#!/bin/bash
# SPDX-FileCopyrightText: 2023 Akito Noguchi
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg fibonacci.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '計算結果: 21'
