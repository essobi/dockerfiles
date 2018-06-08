FROM ubuntu:14.04.3  
#安装中文和英文语言支持  
RUN apt-get update \  
&& apt-get install -y language-pack-zh-hant language-pack-zh-hans language-
pack-en \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
#设置时区和默认语言  
ENV TZ Asia/Shanghai  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8

