## Blog

### 运行  
将撰写的 md 文件放在 src 文件夹下，运行脚本在 bin 文件夹中：  
- 本地版 `python local.py`
- 网络加载版 `python online.py`
- 网络版 `python server.py`
- CCF会议网络版 `python ccf.py` 添加session目录列表

本地版不需要 skin.js ; server 跟 online 的区别是前者用到 cookie 记录了当前主题的选择，更改一次主题会影响全部网页; 而后者主题更改仅影响当前网页，可用于单网页的情况。

### 说明  
- bin  
python 脚本，包括 markdown 解析，转成 html

- config  
blog 本地化需要用到的一些资源，包括本地化 css、mathjax 等。网络版不需要发布此部分，所需资源从网络上加载。  
主要的有 dark.css、light.css、classie.js、skin.js

- src  
存放撰写的 markdown 文件

- posts  
运行后由 md 文件解析生成的 html 文档。  
如果是执行网络版 server.py 则可将该 posts_server 文件夹直接作为静态 Blog 发布；如果执行本地版 local.py 则需要连同 config 文件夹一起发布。

- demo  
网络版的 blog 示例，即生成的 posts_server 文件夹内容
