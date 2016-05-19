# Cmder设置

## 快捷键

- ctrl+w 关闭当前标签
- ctrl+N 新建标签
- ctrl+B 上下分屏 （自定义）
- ctrl+E 左右分屏 （自定义）
- RCtrl+方向键  调正分屏边缘（自定义）
- F11 全屏（自定义）
- Ctrl+Tab 标签间轮换
- Win+Tab 系统应用轮换
- Win+方向键 窗口最大、最小、左边、右边 
- Alt+F4 关闭所有标签
- Ctrl+D 各种登出，ssh登出，关闭当前标签，关闭窗口

## 应用设置

- main
	- monospace关闭防止字体重叠
	- appearance
		- show buttons in tab bar 右下角显示工具栏
	- tabs  
		- always show 显示标签
		- tabs on bottom 标签在底部还是顶部
		- active console only 只显示活动的标签
		- one tab per group 一个分屏组合只显示一个标签
		- template改成 %c  各cmd标签按数字编号  
	- task bar
		- active console only 在任务栏只显示一个标签，
		- show all consoles 是显示多个层叠标签
- startup
	- specified named task 默认启动的shell
- keys&macro 快捷键设置
	- split:duplicate active shell to bottom 往下分屏
	- split:duplicate active shell to right 往右分屏
	- split: move splitter upward 分屏边界上移 
	- split: move splitter downward 分屏边界下移 
	- split: move splitter leftward 分屏边界左移 
	- split: move splitter rightward 分屏边界右移 
	- split: put focus to nearest pane upword 焦点移到最近的上分屏
	- split: put focus to nearest pane downword 焦点移到最近的下分屏
	- split: put focus to nearest pane leftword 焦点移到最近的左分屏
	- split: put focus to nearest pane rightword 焦点移到最近的右分屏
	- full screen 全屏

## 系统设置

[Cmder Github](https://github.com/cmderdev/cmder)

### 添加到右键

管理员模式打开cmder在终端运行  
cmder /register all

### 右键图标不显示

定位到注册表  
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\Cmder  
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\shell\Cmder  
将Icon的值 dir\icons\cmder.ico 改为 dir\Cmder.exe 即可显示图标

### 解决中文错位

输入 `win + alt + p` 或者 在顶部右击点击 settings, 进入设置页面, 去掉 monospace 选项

#### 初始路径

setting-startup-tasks-{cmd} 最后的框中添加 /Desktop 即  
cmd /k "%ConEmuDir%\..\init.bat"  -new_console:d:%USERPROFILE%/Desktop

#### 自定义 bin  

把大部分单个文件的命令行工具放在一个目录，比如 C:\Bin，然后把这个路径放在 Path 上, 在里面添加bat文件，如note.bat  打开notepad++.exe
~~~
@echo off
start "" "D:\Program Files\Notepad++\notepad++.exe"
~~~

#### ls 颜色、中文输出  

1. 下载git （其实是用到msys）将下面的 \bin 和 \cmd文件夹放到环境变量，这样同时有了git（要是不想用git，可以单独把里面的ls.exe和msys-1.0.dll复制到系统的\bin中使用）

2. 实现颜色跟中文, 将cmder\config\aliases中添加：  
ls=ls --show-control-chars -F --color $* 

3. cmder\config\aliases 文件中可以设置命令的别名

~~~
e.=explorer .    #输入e.可以打开当前路径的文件夹  
gl=git log --oneline --all --graph --decorate  $*  #输入gl  可以查看git log信息  
clear=cls   #输入cls，清屏
~~~

#### ssh远程登录

- `plink 登录名@IP `  即可链接到远程主机

如果在putty中已经存储了一个 session, 例如名字叫 mypc  则可以用
`plink mypc`  来登录或者是`plink mypc -l 用户名 -pw 密码`；需要将 plink.exe、putty.exe 放到系统 \bin 中

- git 的 mysys 中自带了 ssh.exe ,可用 `ssh -t root@12.23.34.45 -p 22` 设置自定义端口

- 可以在 cmder\config\aliases 中添加 **`sshroot = ssh name@IP `**, 每次运行 sshroot 即可

#### 中文编码显示乱码

可能会有中文编码显示乱码，因为 cmd 默认的是 GB2312 编码，可以在 cmd 中输入 chcp 命令会看到当前代码页是 936；要换成UTF-8 编码可以输入命令 chcp 65001；但是这种方式只能当前有效，关闭后就会回到 936

在 cmd 的属性中把字体换成 Lucida Console 可永久变成 utf-8 的 65001

#### 编码问题解决

在 cmder/vendor/init.bat 最后一行添加命令就是在 cmd 中执行的作为默认设置，UTF-8 支持则添加  
`chcp 65001 > nul` 表示更改分页编码，同时将输出信息隐藏

同时添加下面这句，防止 python 出现 LookupError: unknown encoding: cp65001 的错误  

` @set PYTHONIOENCODING=utf-8` 
