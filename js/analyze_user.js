$(function() {
  $(document).ready(function() {
    $('#check_user').button().click(function() {
      var user = $('#user_name').val();
      console.log(user);
      // コメント中の単語の出現数を取得
      $('#error_message').empty()
      util.getJson(
        '/check_twitter/json/analyze_user/' + user,
        {},
        function (err, result) {
          if (err) {
            $('#error_message').append(err)
            return;
          }
          if (result.result) {
            $('#error_message').append(result.error)
            return;
          }
          $('#user_info').empty();
          $('#user_info').append('<p><img src="' + result.user.profile_image_url + '"/></p>');
          var desc = result.user.description;
          if (desc) {
            desc = desc.replace(/[\n]/g, "<br />");
          }
          $('#user_info').append('<div class="balloon-3-top-left">' + desc + '</div>');

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