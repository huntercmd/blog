#coding=utf-8

"""
网络版css、mathjax、font-awesome，带返回顶部

用mistune来解析md文件，自带侧边目录，不需要设置[TOC]

python  run_local.py


输出：posts文件夹下 index.html、XX.html  YY.html ...

返回的html文件中用到自己定义的信息，如css，mathjax等详情见 html_head、html_footer部分

"""

import shutil
import os
import mistune
import sys
reload(sys)
sys.setdefaultencoding('utf8')#解决字符串乱码问题

top_level = 1
header_info = []


html_head = """
<head>
<meta name="HunterCmd" charset="utf-8">

<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
<link id="light" rel="stylesheet" type="text/css" href="https://gitcdn.xyz/repo/huntercmd/blog/master/config/css/light.css">
<link id="dark" rel="stylesheet" type="text/css" href="https://gitcdn.xyz/repo/huntercmd/blog/master/config/css/dark.css" disabled/>

<script src="https://gitcdn.xyz/repo/huntercmd/blog/master/config/css/classie.js"></script>


<title>LQG</title>
</head>

<body class="cbp-spmenu-push">

<nav class="cbp-spmenu cbp-spmenu-vertical cbp-spmenu-left" id="menu-s1" style="width: 320px;overflow: auto;
">

"""


html_footer = """

<div class="home">
<i title='主页' onclick="location.href='../index.html'"><i class="fa fa-home fa-lg"></i></i>
</div>

<div class="toc">
<i id="showLeftPush" title='目录'><i class="fa fa-list fa-lg"></i></i>
</div>

<!-- Classie - class helper functions by @desandro https://github.com/desandro/classie -->
<script>
	var menuLeft = document.getElementById( 'menu-s1' ),
		showLeftPush = document.getElementById( 'showLeftPush' ),
		body = document.body;

	showLeftPush.onclick = function() {
		classie.toggle( this, 'active' );
		classie.toggle( body, 'cbp-spmenu-push-toright' );
		classie.toggle( menuLeft, 'cbp-spmenu-open' );
		disableOther( 'showLeftPush' );
	};
</script>

<div class="go-top" >
<i title='顶部' onclick="window.scrollTo('0', '0')"><i class="fa fa-angle-double-up fa-2x"></i></i>
</div>

<div class="theme" >
<i title='主题' onclick="setStyle()"><i class="fa fa-adjust fa-lg"></i></i>
</div>

<!-- 更换theme -->
<script type="text/javascript">
function setStyle(){
    if(document.getElementById("dark").disabled){
        document.getElementById("light").disabled = true;
        document.getElementById("dark").disabled = false;
        }
    else{
        document.getElementById("dark").disabled = true;
        document.getElementById("light").disabled = false;
        }
    }
</script>

<div id="footer">

  <p> <i class="fa fa-envelope-o fa-1x"></i>:&nbsp huntercmd@163.com &nbsp Published under<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh"> (CC) BY-NC-SA 3.0</a></p>

  <p>&copy; 2013 HunterCmd &nbsp <a href="http://huntercmd.github.io"><i class="fa fa-github fa-1x"></i>
  </p>
</div>

</body>
"""



def index(titlelist):#将src中文件按照md列表格式写成index.md文件
	index_text = "# 目录\n"
	for item in titlelist:#md文件的标题列表
		item = item.decode("GBK")
		title = item.split(".")
		index_text += ("- [" + title[0] + "](./posts/" + item + ")\n")
	return index_text


####以下是md解析相关
class headerRenderer(mistune.Renderer):#更换mistune中header输出，添加id属性
	def header(self, text, level, raw=None):
		global top_level, header_info
		header_info.append([level, raw, text])
		top_level = level if level < top_level else top_level
		return '<h%d id="%s">%s</h%d>\n' % (level, raw, text, level)


def header_md():#输出md形式的header列表
	global top_level, header_info
	toc_md = '# Table of contents \n'
	for i in range(len(header_info)):
		toc_md += '%s- [%s](#%s)\n' %( (header_info[i][0]-top_level)*'    ', header_info[i][2], header_info[i][1])#按header等级的缩进量写成md列表

	top_level = 1 #重新设定
	header_info = []
	return toc_md


def md2html(context_md):
	renderer = headerRenderer()
	md = mistune.Markdown(renderer=renderer)
	context_html = md.render(context_md) #解析md文件正文，修改mistune中header输出，添加id

	toc_html = mistune.markdown(header_md())#解析md形式的目录列表

	return html_head + toc_html +"</nav>"+ context_html + html_footer


if __name__=='__main__':

	mddir = os.getcwd()[:-3]+"src" #去掉路径中 bin，转到 src路径中
	mdlist = os.listdir(mddir)
	outdir = os.getcwd()[:-3]+"posts_online" #生成文件的路径
	if os.path.exists(outdir):
		shutil.rmtree(outdir)#删除已有的posts文件夹
	os.mkdir(outdir)#创建
	index_md = "# 目录\n" #自动生成目录

#生成各html文件，统计目录
	for item in mdlist:
		f = open( mddir+"\\"+item, 'r')#打开文件
		context_md = f.read()
		title = item.strip().split('.')
		outfile = open(outdir+"\\"+title[0]+'.html', 'w')#创建html
		outfile.write( md2html(context_md) )#解析输出
		print title[0]+" done!"
		f.close( )
		outfile.close( )

		title[0] = title[0].decode("GBK")#防止中文标题乱码
		index_md += ("- [" + title[0] + "](./" + title[0] + ".html)\n")

	outfile = open( outdir+"\\index.html", 'w')
	outfile.write( md2html(index_md) )#解析输出
	outfile.close( )
	print "All OK"
