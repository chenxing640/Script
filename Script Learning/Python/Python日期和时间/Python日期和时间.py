#!/usr/bin/python
#coding=utf-8

#Python程序能用很多方式处理日期和时间。转换日期格式是一个常见的例行琐事。
#Python有一个 time 和 calendar 模组可以帮忙。

#什么是Tick？
#时间间隔是以秒为单位的浮点小数。
#每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
#Python附带的受欢迎的time模块下有很多函数可以转换常见日期格式。
#如函数time.time()用ticks计时单位返回从12:00am, January 1, 1970(epoch) 开始的记录的当前操作系统时间, 如下实例:

import time

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

#什么是时间元组？
#很多Python函数用一个元组装起来的9组数字处理时间:
#上述也就是struct_time元组。这种结构具有如下属性：
#序号     属性      说明        值
#0       tm_year  4位数年      2008
#1       tm_mon   月           1 到 12
#2       tm_mday  日           1 到 31
#3       tm_hour  时           0 到 23
#4       tm_min   分钟         0 到 59
#5       tm_sec   秒           0 到 61 (60或61 是闰秒)
#6       tm_wday  一周的第几日   0到6 (0是周一)
#7       tm_yday  一年的第几日   1 到 366(儒略历)
#8       tm_isdst 夏令时        -1, 0, 1, -1是决定是否为夏令时的旗帜

#获取当前时间
#从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

localTime = time.localtime(time.time())
print "Local current time: ", localTime

#获取格式化的时间
#你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():

localTime = time.asctime(time.localtime(time.time()))
print "Local current time: ", localTime

#获取某月日历
#Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar
cal = calendar.month(2016, 2)
print "Here is the calendar: "
print cal

#Time模块
#Time模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的：
#序号	函数及描述
#1	time.altzone
#返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
#2	time.asctime([tupletime])
#接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
#3	time.clock( )
#用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
#4	time.ctime([secs])
#作用相当于asctime(localtime(secs))，未给参数相当于asctime()
#5	time.gmtime([secs])
#接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
#6	time.localtime([secs])
#接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
#7	time.mktime(tupletime)
#接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
#8	time.sleep(secs)
#推迟调用线程的运行，secs指秒数。
#9	time.strftime(fmt[,tupletime])
#接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
#10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
#根据fmt的格式把一个时间字符串解析为时间元组。
#11	time.time( )
#返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
#12	time.tzset()
#根据环境变量TZ重新初始化时间相关设置。
#Time模块包含了以下2个非常重要的属性：
#序号	属性及描述
#1	time.timezone
#属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
#2	time.tzname
#属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

#日历（Calendar）模块
#此模块的函数都是日历相关的，例如打印某月的字符月历。
#星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
#序号	函数及描述
#1	calendar.calendar(year,w=2,l=1,c=6)
#返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
#2	calendar.firstweekday( )
#返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
#3	calendar.isleap(year)
#是闰年返回True，否则为false。
#4	calendar.leapdays(y1,y2)
#返回在Y1，Y2两年之间的闰年总数。
#5	calendar.month(year,month,w=2,l=1)
#返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
#6	calendar.monthcalendar(year,month)
#返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
#7	calendar.monthrange(year,month)
#返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
#8	calendar.prcal(year,w=2,l=1,c=6)
#相当于 print calendar.calendar(year,w,l,c).
#9	calendar.prmonth(year,month,w=2,l=1)
#相当于 print calendar.calendar（year，w，l，c）。
#10	calendar.setfirstweekday(weekday)
#设置每周的起始日期码。0（星期一）到6（星期日）。
#11	calendar.timegm(tupletime)
#和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
#12	calendar.weekday(year,month,day)
#返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。

#其他相关模块和函数
#在Python中，其他处理日期和时间的模块还有：
#datetime模块 https://docs.python.org/2/library/datetime.html#module-datetime
#pytz模块     http://www.twinsun.com/tz/tz-link.htm
#dateutil模块 http://labix.org/python-dateutil

