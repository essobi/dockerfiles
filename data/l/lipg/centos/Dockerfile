FROM centos:6  
# 添加中文支持  
RUN localedef -c -f UTF-8 -i zh_CN zh_CN \  
&& localedef -c -f UTF-8 -i zh_CN zh_CN.utf8 \  
&& localedef -c -f GB18030 -i zh_CN zh_CN.gb18030 \  
&& localedef -c -f GB2312 -i zh_CN zh_CN.gb2312 \  
&& localedef -c -f GBK -i zh_CN zh_CN.gbk \  
&& localedef -c -f UTF-8 -i zh_HK zh_HK \  
&& localedef -c -f BIG5-HKSCS -i zh_HK zh_HK.big5hkscs \  
&& localedef -c -f UTF-8 -i zh_HK zh_HK.utf8 \  
&& localedef -c -f UTF-8 -i zh_SG zh_SG \  
&& localedef -c -f GB2312 -i zh_SG zh_SG.gb2312 \  
&& localedef -c -f GBK -i zh_SG zh_SG.gbk \  
&& localedef -c -f UTF-8 -i zh_SG zh_SG.utf8 \  
&& localedef -c -f UTF-8 -i zh_TW zh_TW \  
&& localedef -c -f BIG5 -i zh_TW zh_TW.big5 \  
&& localedef -c -f EUC-TW -i zh_TW zh_TW.euctw \  
&& localedef -c -f UTF-8 -i zh_TW zh_TW.utf8  
#设置时区和语言环境变量  
ENV TZ Asia/Shanghai  
ENV LANG zh_CN.UTF-8  
ENV LC_ALL zh_CN.UTF-8  

