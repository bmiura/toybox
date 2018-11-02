## lifegame.py と lifegame_new.py
lifegame.pyは2016年9月に書いたもの。  
lifegame_new.pyは2018年10月にlifegame.pyをリファクタしたもの。  
動作は同じ。  
生物ありが白。なしが黒。  
`esc` : 終了  
`方向キー` : 選択中マスの移動  
`space` : 選択中マスを反転  
`s` : スタート/停止  
`n` : 次の世代へ  
`r` : ランダム初期化  
`c` : 全消去  
`k` : 加速/減速  

## transhelper.js
論文をgoogle翻訳にかけるときに便利なブックマークレット。

## check_gpu.py
1. `nvidia-smi`でどのGPUでどのプロセスが動いてるか調べる  
2. `/proc/{pid}/cgroup`を見てそのプロセスがどのdockerコンテナ由来か調べる  
3. `docker ps`でコンテナidからコンテナ名を調べる  
4. 表示する  

をするだけのプログラム。使用宣言してないのにこっそりGPU使ってる人を割り出そうな。
