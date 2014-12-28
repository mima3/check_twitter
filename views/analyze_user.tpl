<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
  <title>ツイッターユーザの解析</title>
  <link rel="stylesheet" href="/check_twitter/js/jqcloud/jqcloud.css" type="text/css" />
  <link rel="stylesheet" href="/check_twitter/base.css" type="text/css" />
  <link rel="stylesheet" href="/check_twitter/js/jquery/jquery-ui.min.css" type="text/css" />
  <script type="text/javascript" src="/check_twitter/js/jquery/jquery-1.11.1.min.js"></script>
  <script type="text/javascript" src="/check_twitter/js/jquery/jquery-ui-1.10.4.min.js"></script>
  <script type="text/javascript" src="/check_twitter/js/jqcloud/jqcloud-1.0.4.min.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/blockui/jquery.blockUI.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/util.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/analyze_user.js" ></script>
</head>
<body>
  <div id="contents">
    <h1>ツイッターユーザの解析</h1>
    <p>ユーザ名：<input id="user_name" type="text" name="name" size="30" maxlength="20"></input></p>
    <p><button id="check_user">ユーザのチェック</button></p>
    <div id="error_message" class="error"></div>
    <div id="termTagCloud" style="width: 100%; height: 480px;"></div>
</body>
</html>
