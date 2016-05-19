# markdown文档转本地html及pdf

## 安装 markdown 解析器
找个简单的Python下的markdown解析器 [mistune][1]安装:  
`$ pip install mistune`。

## 运行脚本
利用 md2html.py 来解析成 html 文档, html 文件名自动生成：  
`python md2html.py XX.md YY.md ZZ.md  ...`

注意 html 需要一个本地的 css 文件、mathjax 可以本地化（目前还需要网络）、有返回顶部的功能、用到 [font-awesome][4] 网络图标（也可本地化）

默认html中自动生成目录

## 使用 wkhtmltopdf 将 html 转为 pdf
首先利用上面方法生成 html 文件，然后使用[wkhtmltopdf][3]来生成 pdf:  
`wkhtmltopdf XX.html  XX.pdf`

可以自动生成 pdf 的书签

注意 生成的 pdf 对 mathjax 公式支持不好


## 本地化使用

双击 .bat 脚本输入md文件名即可实现转化

- 2html_local.bat 转为本地版html
- 2html_online.bat 转为网络版html
- 2pdf.bat 临时转为本地html再转为pdf,自带书签,没有返回顶部,css字体黑色，无背景色


作者 [Leequangang][2]     
2015 年 5月 4日 

[1]: https://github.com/lepture/mistune
[2]: leequangang@gmail.com
[3]: https://github.com/wkhtmltopdf/wkhtmltopdf
[4]: http://fontawesome.io/