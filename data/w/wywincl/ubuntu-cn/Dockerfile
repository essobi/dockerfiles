FROM ubuntu:14.04  
MAINTAINER wywincl <wywincl@126.com>  
  
# 使用root用户  
USER root  
  
# 使用Ubuntu官方的Apt-get源  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu trusty-updates main universe\n"
>> /etc/apt/sources.list  
  
# 更新源  
RUN apt-get update -qqy  
  
# 配置中文语言  
ENV LANGUAGE zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
ENV LC_ALL=zh_CN.UTF-8  
RUN /usr/share/locales/install-language-pack zh_CN \  
&& locale-gen zh_CN.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get -qqy --no-install-recommends install language-pack-zh-hans  
  
# 安装基本字体  
RUN apt-get -qqy --no-install-recommends install \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable  
  
# 安装文泉驿微米黑字体  
RUN apt-get -qqy install ttf-wqy-microhei \  
&& ln /etc/fonts/conf.d/65-wqy-microhei.conf /etc/fonts/conf.d/69-language-
selector-zh-cn.conf  
  
# 设置时区  
ENV TZ "PRC"  
RUN echo "Asia/Shanghai" | tee /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
# 添加具有免密码sudo权限的普通用用户  
RUN useradd worker --shell /bin/bash --create-home \  
&& usermod -a -G sudo worker \  
&& echo 'worker ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'worker:pa55w0rd' | chpasswd  
  
# 安装其他基础软件  
RUN apt-get -qqy --no-install-recommends install curl wget  
  
# 删除不必要的软件和Apt缓存包列表  
RUN apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  

