1.使用logging module来记录程序调试，而不要使用print.
2.列表常见方法：len(),index(), append(), sort(), remove(), pop()
3.字典常见方法：keys(), values(), items(), get(), setdefault()
4.字符串常见方法：upper(), lower(), isupper(), islower(), startswith(), endswith(), join(), split(), ljust(), rjust(), center(), strip(), rstrip(),lstrip()
5.模式匹配，正则表达式： import re, re.compile(), search(), group(),findall(), sub(). |匹配许多中的一个, ?可选匹配, *匹配零次到多次,+匹配一次到多次,{}匹配特定次数,默认为贪心匹配，
  {}后加？为非贪心匹 配,^开头表明匹配必须发生在被查找文本开始处,$结尾匹配, .通配符，匹配除换行之外的所有字符. re.VERBOSE忽略正则表达式中的空白符和注释,[]里加字符将匹配字符分类
6.读写文件:os.path:join(),getcwd(),makedirs(),abspath(),isabs(),basename(), dirname(),listdir(),exists(),isdir(),isfile().
  open() w写模式从头开始,a添加模式在末尾添加文本, read(),readlines(), shelve module
7.组织文件：shutil模块，chdir(),shutil.copy(),move().os.unlink(),rmdir(),rmtree().send2trash模块.zipfile模块