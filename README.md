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
### talker.pyとlistener.py  
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

---

### problem.pyとanswer.py  

```
端末1$ ros2 run mypkg answer
```

端末1で先にanswer.pyを実行しておいてください.

```
端末2$ ros2 run mypkg problem
[INFO] [1703927729.597357600] [Number]: Publishing: 968
[INFO] [1703927730.583074300] [Number]: Publishing: 827
[INFO] [1703927731.581323200] [Number]: Publishing: 925
[INFO] [1703927732.581826200] [Number]: Publishing: 612
[INFO] [1703927733.581454700] [Number]: Publishing: 883
                           .  
                           .  
[INFO] [1703927849.396617800] [Number]: finish
```

表示される整数はランダムです.
その後、端末1に戻ると結果が表示されます.

```
[INFO] [1703927729.629098700] [Answer]: 968 は素数ではないです
[INFO] [1703927730.586846100] [Answer]: 827 は素数です
[INFO] [1703927731.582240900] [Answer]: 925 は素数ではないです
[INFO] [1703927732.583410000] [Answer]: 612 は素数ではないです
[INFO] [1703927733.582418700] [Answer]: 883 は素数です
                           .  
                           .  
```

problem.pyは60秒が経過すると停止します.

---

### fibonacci.py

```
$ ros2 run mypkg fibonacci
[INFO] [1703928735.922960600] [Fibonacci]: 計算結果: 0
[INFO] [1703928736.911557900] [Fibonacci]: 計算結果: 1
[INFO] [1703928737.912669500] [Fibonacci]: 計算結果: 1
[INFO] [1703928738.913622300] [Fibonacci]: 計算結果: 2
[INFO] [1703928739.913252300] [Fibonacci]: 計算結果: 3
[INFO] [1703928740.912661300] [Fibonacci]: 計算結果: 5
[INFO] [1703928741.912101900] [Fibonacci]: 計算結果: 8
[INFO] [1703928742.913424400] [Fibonacci]: 計算結果: 13
                           .  
                           .  
```

実行後上記のように表示.  
終了するときは`ctrl+C`を入力.  

## テスト環境

* Ubuntu 20.04
* ROS2 foxy

## 権利関係

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.  
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、  
本人の許可を得て自身の著作としたものです.  
    * [ryuichiueda/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/)
    * [ryuichiueda/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/)
    * [ryuichiueda/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/)
    * [ryuichiueda/my_slides/robosys_2022/lesson11](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/)
* © 2023 Akito Noguchi
