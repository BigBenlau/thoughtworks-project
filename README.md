# Game of life
ThoughtWorks project 20190616   
第八组 刘俊杰 汤叡欣  
编程语言：python

## 实现功能
- 实现核心逻辑
- 用界面展示结果 
- 自定义设置 （command line）
    - 指定初始图案
        - Blinker (周期细胞)
        - Toad （周期细胞）
        - Glider （飞船细胞）
        - Small Exploder （扩展细胞）
    - 可设定格子数量
    - 可控制动画速度

## 使用说明
- 主代码： project_pygame.py
    - 进行初始化设置
        - grid setup ：设置格子数量 enter表示默认 50*50
        - state duration ： 状态保持时间 单位秒 
        - select map : 选择图案 enter表示默认 Small Exploder
    - 自动运行
    - start stop按钮 暂不可用
- 测试代码：test.py

## 自定义设置参考
gride setup --- state duration --- select map
- default default --- 2 --- default
- default default --- 1 --- Glider
- 28 28 --- 1 --- Glider

## Reference

- game of life 图案参考 https://haojunsui.github.io/2016/06/21/game-of-life/
- 单元测试教程 https://blog.csdn.net/huilan_same/article/details/52944782
- pygame 
    - game of life https://codereview.stackexchange.com/questions/131689/beginners-pygame-conways-game-of-life 
    - button https://pythonprogramming.net/pygame-buttons-part-1-button-rectangle/