# mypkg
[![test](https://github.com/akitonoguchi/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/akitonoguchi/mypkg/actions/workflows/test.yml) [![prime_test](https://github.com/akitonoguchi/mypkg/actions/workflows/prime_test.yml/badge.svg)](https://github.com/akitonoguchi/mypkg/actions/workflows/prime_test.yml) [![fibonacci_test](https://github.com/akitonoguchi/mypkg/actions/workflows/fibonacci_test.yml/badge.svg)](https://github.com/akitonoguchi/mypkg/actions/workflows/fibonacci_test.yml)

ロボットシステム学で使用したros2について

# リポジトリ内のノード

### talker.py
* パブリッシャ側のノード.秒単位で数字をカウントし,  
トピック`/countup`を通じて送信します.

### listener.py
* サブスクライバ側のノード.トピック`/countup`を通してtalker.pyから  
メッセージを受けとり、内容を表示します.

### problem.py
* パブリッシャ側のノード. 0~999 までのランダムな整数を生成しその整数を表示、  
またトピック`/random_number`を通して内容を送信します.
* 60秒経過するとノードが停止します.

### answer.py
* サブスクライバ側のノード.トピック`/random_number`を通してproblem.pyから  
メッセージを受け取り、受け取った整数が素数かそうではないかを判定します.
