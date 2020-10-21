[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/tonyjxc/ikatago/blob/master/ddos_2.ipynb)
# ikatago
connect to aistudio automatically with ikatago coded by kinfkong  

在学会利用ikatago之后，利用本软件可以使你更便捷地连接到百度的katago上  

# 本软件集合的功能
1.自动存储百度账号的cookie在本地（不会上传到我这里，保证账号的安全性）  
2.登录aistudio并通过js刷新页面来重复提交请求以获得gpu版本  
3.获取gpu后自动跳转，并运行项目  

# 我要做什么
## 第一次使用时的初始化
1.成功运行过kinfkong的ikatago 设置过自己的账号密码  
2.运行cookie.py，按照步骤登录百度账号  
3.运行aistudio_withgui.py。检查浏览器能否正常启动ikatago  
4.正常使用ikatago  

## 继续使用
1.启动aistudio_withgui.py/aistudio_nogui.py （一个带gui、一个不带gui）  
2.按照提示使用，软件的速度取决于aistudio是否给你留有了足够的gpu  
3.正常使用

# 其它插件
## chrome获得aistudio GPU的插件  
### 如何使用  
1.chrome 开发者模式，加载已解压的拓展程序  
2.加载插件所在的文件夹即可  

使用时在项目的界面会自动弹出窗口开始运行，在获取到gpu后即自动进入  
本软件刷新率为2s一次，想要更改的可以自行修改代码  
123456