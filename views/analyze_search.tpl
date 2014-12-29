<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
  <title>ツイッター検索結果の解析</title>
  <link rel="stylesheet" href="/check_twitter/js/jqcloud/jqcloud.css" type="text/css" />
  <link rel="stylesheet" href="/check_twitter/base.css" type="text/css" />
  <link rel="stylesheet" href="/check_twitter/js/jquery/jquery-ui.min.css" type="text/css" />
  <script type="text/javascript" src="/check_twitter/js/jquery/jquery-1.11.1.min.js"></script>
  <script type="text/javascript" src="/check_twitter/js/jquery/jquery-ui-1.10.4.min.js"></script>
  <script type="text/javascript" src="/check_twitter/js/jqcloud/jqcloud-1.0.4.min.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/blockui/jquery.blockUI.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/util.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/analyze_search.js" ></script>
</head>
<body>
  <div id="contents">
    <h1>ツイッター検索結果の解析</h1>
    <p>検索文字：<input id="keyword" type="text" name="name" size="30" maxlength="20"></input></p>
    <p><button id="check_keyword">検索文字のチェック</button></p>
    <div id="error_message" class="error"></div>
    <div id="user_info"></div>
    <div id="termTagCloud" style="width: 100%; height: 480px;"></div>
    <table class="normal">
      <thead>
        <th>単語</th>
        <th>出現数</th>
      </thead>
      <tbody id="tblTerms">
      </tbody>
    </table>
</body>
</html>
