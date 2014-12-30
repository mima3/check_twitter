<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
  <title>ツイッター位置情報の解析</title>
  <link rel="stylesheet" href="/check_twitter/js/jqcloud/jqcloud.css" type="text/css" />
  <link rel="stylesheet" href="/check_twitter/base.css" type="text/css" />
  <link rel="stylesheet" href="/check_twitter/js/jquery/jquery-ui.min.css" type="text/css" />
  <script type="text/javascript" src="/check_twitter/js/jquery/jquery-1.11.1.min.js"></script>
  <script type="text/javascript" src="/check_twitter/js/jquery/jquery-ui-1.10.4.min.js"></script>
  <script type="text/javascript" src="/check_twitter/js/jqcloud/jqcloud-1.0.4.min.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/blockui/jquery.blockUI.js" ></script>
  <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false&language=ja"></script>
  <script type="text/javascript" src="/check_twitter/js/util.js" ></script>
  <script type="text/javascript" src="/check_twitter/js/analyze_locate.js" ></script>
</head>
<body>
  <div id="contents">
    <h1>ツイッター位置情報の解析</h1>
    <div id="map_canvas" style="width: 100%; height: 300px"  class="ui-shadow"></div>
    <select name="radius" id="selectRadius">
      <option value="500">500m</option>
      <option value="1000">1km</option>
      <option value="3000">3km</option>
      <option value="5000">5km</option>
    </select>
    <p>経度：<span id="lat"></span></p>
    <p>緯度：<span id="lng"></span></p>
    <p><button id="check_place">位置情報のチェック</button></p>
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
