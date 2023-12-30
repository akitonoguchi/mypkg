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

### fibonacci.py
* フィボナッチ数列の値を計算するノードです.  計算結果を順に表示します.

## 実行手順と実行例
### talkerとlistener 
* `ros2 run`で実行する方法  

```
端末1$ ros2 run mypkg talker  
端末2$ ros2 run mypkg listener  
[INFO] [1703926331.295823100] [listener]: Listen: 0  
[INFO] [1703926331.758097600] [listener]: Listen: 1  
[INFO] [1703926332.258281500] [listener]: Listen: 2  
[INFO] [1703926332.759116300] [listener]: Listen: 3  
[INFO] [1703926333.260979500] [listener]: Listen: 4  
[INFO] [1703926333.758617800] [listener]: Listen: 5  
                         .  
                         .
```
実行後上記のように表示.    
終了するときは`ctrl+C`を入力.

* `ros2 launch`で実行する方法  

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/akito/.ros/log/2023-12-30-17-59-17-233176-akitonoguchi99-17261
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [17263]
[INFO] [listener-2]: process started with pid [17265]
[listener-2] [INFO] [1703926758.215602600] [listener]: Listen: 0
[listener-2] [INFO] [1703926758.694193700] [listener]: Listen: 1
[listener-2] [INFO] [1703926759.194986500] [listener]: Listen: 2
[listener-2] [INFO] [1703926759.695048500] [listener]: Listen: 3
[listener-2] [INFO] [1703926760.194053000] [listener]: Listen: 4
[listener-2] [INFO] [1703926760.697104100] [listener]: Listen: 5
                                .  
                                .  
``` 
実行後上記のように表示.  
終了するときは`ctrl+C`を入力.  
