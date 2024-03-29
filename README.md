## Script

[![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat)](LICENSE)&nbsp;

编写 Shell, Python, Ruby 等一些实用脚本。


## Group (ID:155353383)

<div align=left>
&emsp; <img src="https://github.com/chenxing640/Script/raw/master/images/qq155353383.jpg" width="30%" />
</div>


## iOS Automated Packaging Scripts

* [iOS Automated Packaging Scripts](https://github.com/chenxing640/Script/tree/master/iOS%20Automated%20Packaging%20Scripts)

在一个 Base 工程中，通过不断复制 .xcodeproj 和 修改 xcodeproj/project.pbxproj，为 project.pbxproj 文件添加资源、支持的架构、Target 名称、动静态库、修改最小兼容部署等，修改 Info.plist 的 Bundle identifier, QueriesSchemes, URLTypes, Orientations，还有修改包的 ICON 和初始化参数，从而输出各种需求的 ipa 包。

1. XCPkg Args 

此脚本项目由本人独立开发完成，依赖 Python 和 Ruby 库：biplist, mod_pbxproj, rb_modproj。

自编写控制脚本 (PkgController.sh) 在内总计有26个脚本，再加上调试，历时一个多月，其过程非常地辛苦！！！

2. XCPkg Encryption

将 XCPkg 所有脚本进行加密处理，并集成到[ Mac应用 - IPAPkgTool ](https://github.com/chenxing640/IPAPkgTool)。


## ExcelTxtScript

* [ExcelTxtScript](https://github.com/chenxing640/Script/tree/master/ExcelTxtScript)

一个将 excel 文件 (.xlsx) 和 txt 文件 (.txt) 互相转换一个脚本项目，并集成到[ Mac应用 - MacExcelTool ](https://github.com/chenxing640/MacExcelTool)。


## Recommend

- [Package IPA Script](https://github.com/chenxing640/Script/blob/master/Shell/CXPackageUtils.sh) - 打包 ipa 脚本
- [Resign App Script](https://github.com/chenxing640/Script/blob/master/Shell/CXCodesign.sh) - 重签名 app 脚本
- [App Icon Generator](https://github.com/chenxing640/Script/blob/master/Shell/CXICONMaker.sh) - 生成 App 各个 Icon 尺寸的脚本


## Script Learning
 
 - [Script Learning](https://github.com/chenxing640/Script/tree/master/Script%20Learning) - 脚本学习Demo
