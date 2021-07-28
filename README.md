1. install library
```sh
pip install -r requirements.txt
```
2. LanguageTranslater@IBM Cloudページから「API鍵」と「URL」をコピーして10行目/11行目をそれぞれ置き換え
3. 実行

* 使い方その１
```sh
$ ./lt.py banana
バナナ
```

* 使い方その２
```sh
$ ./lt.py バナナ -m ja-en
banana
```

* 使い方その３(pipe使えます)
```sh
$ cat test2.txt
Hello.
It's a nice day, isn't it?
I would like to go on a trip this day.
$ cat test2.txt | ./lt.py
やぁ
今日はいい天気ですね。
私はこの日旅行に行きたいものだ。
```

