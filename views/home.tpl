<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
  <title>ツイッターチェック</title>
  <link rel="stylesheet" href="/analyze_election/base.css" type="text/css" />
</head>
<body>
  <div id="contents">
    <h1>ツイッターの解析</h1>
    %if access_token:
      <p>Hello {{access_token['screen_name']}}</p>
    %end
    <p><a href="/check_twitter/login">ログイン</a>　<a href="/check_twitter/logout">ログアウト</a></p>
    <p><a href="/check_twitter/analyze_user">ツイッターユーザの解析</a></p>
    <p>指定のユーザがよくつぶやく単語を抽出します。</p>
    <p><a href="/check_twitter/analyze_search">ツイッター検索結果の解析</a></p>
    <p>指定のキーワードの検索結果を含むツイートに含まれる単語を抽出します。</p>
  </div>
</body>
</html>
