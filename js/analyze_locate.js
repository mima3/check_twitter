$(function() {
  $(document).ready(function() {
    var map = null;
    var circle = null;
    var curPos = new google.maps.LatLng(35.709984, 139.810703);
    var opts = {
      zoom: 13,
      center: curPos,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map_canvas'), opts);
    infowindow_list = [];
    google.maps.event.addListener(map, "drag", function() {
      // ドラッグイベント
      curPos = map.getCenter();
      drawCircle();
      var lat = curPos.lat();
      var lng = curPos.lng();
      $('#lat').empty();
      $('#lat').append(lat);
      $('#lng').empty();
      $('#lng').append(lng);
    });

    /**
     * googleマップに選択した範囲の円を記述する
     */
    function drawCircle() {
      var r = parseInt($('#selectRadius').val());
      var circleOpts = {
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 1,
        fillColor: '#FF0000',
        center: curPos,
        map: map,
        radius: r
      };
      if (circle) {
        circle.setMap(null);
      }
      circle = new google.maps.Circle(circleOpts);

    }
    /**
     * 検索位置の半径の変更
     */
    $('#selectRadius').on('change', function() {
      if (!map) {
        return;
      }
      if (!curPos) {
        return;
      }
      drawCircle();
    });

    $('#check_place').button().click(function() {
      console.log('check_place');

      // コメント中の単語の出現数を取得
      $('#error_message').empty()
      util.getJson(
        '/check_twitter/json/analyze_locate',
        {
          lat : curPos.lat(),
          lng : curPos.lng(),
          radius: parseInt($('#selectRadius').val()) / 1000 + 'km'
        },
        function (err, result) {
          console.log(err);
          console.log(result);
          for (var i = 0; i < infowindow_list.length; ++i) {
            infowindow_list[i].close();
          }

          infowindow_list = []
          if (err) {
            $('#error_message').append(err)
            return;
          }
          if (result.result) {
            $('#error_message').append(result.error)
            return;
          }
          for (var i = 0; i < result.statuses.length; ++i) {
            console.log(result.statuses[i]);
            var coordinates = result.statuses[i].geo.coordinates;
            var text = '<img src="'+ result.statuses[i].user.profile_image_url + '" width="16" height="16""/>' + result.statuses[i].text;
            var infowindow = new google.maps.InfoWindow({
              content: text,
              position: new google.maps.LatLng(coordinates[0], coordinates[1])
            });
            infowindow.open(map);
            infowindow_list.push(infowindow);
          }
          // 
          // タグクラウド作成
          $('#termTagCloud').empty();
          $('#termTagCloud').jQCloud(result.data);
          
          // テーブルの作成
          var tbl = $('#tblTerms');
          tbl.empty();
          for (var i = 0; i < result.data.length; ++i ) {
            var tr = $('<tr/>');
            $('<td>' + result.data[i].text + '</td>').appendTo(tr);
            $('<td>' + result.data[i].weight + '</td>').appendTo(tr);
            tr.appendTo(tbl);
          }
          //$('#termTagCloud').jQCloud(result);
          //$('#termsTable').addRowData('1' , result);
        },
        function() {
          $.blockUI({ message: '<img src="/analyze_election/img/loading.gif" />' });
        },
        function() {
          $.unblockUI();
        }
      );
    });
  });
});