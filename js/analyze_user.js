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
        function (errCode, result) {
          console.log(errCode);
          console.log(result);
          if (errCode) {
            $('#error_message').append(errCode)
            return;
          }
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