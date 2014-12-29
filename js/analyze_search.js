$(function() {
  $(document).ready(function() {
    $('#check_keyword').button().click(function() {
      var keyword = $('#keyword').val();
      console.log(keyword);
      // 検索結果中の単語の出現数を取得
      $('#error_message').empty()
      util.getJson(
        '/check_twitter/json/analyze_search',
        {
          keyword : keyword
        },
        function (err, result) {
          if (err) {
            $('#error_message').append(err)
            return;
          }
          if (result.result) {
            $('#error_message').append(result.error)
            return;
          }

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