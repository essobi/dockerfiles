FROM lihaixin/sshd  
MAINTAINER Haixin Lee <docker@lihaixin.name>  
  
# 使用root用户  
USER root  
  
# 更新源  
RUN apt-get update -y  
  
# 配置语言  
ENV LANGUAGE zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
ENV LC_ALL=zh_CN.UTF-8  
RUN /usr/share/locales/install-language-pack zh_CN \  
&& locale-gen zh_CN.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get -y --no-install-recommends install language-pack-zh-hans  
  
# 安装基本字体  
RUN apt-get -y --no-install-recommends install \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable  
  
# 安装文泉驿微米黑字体  
RUN apt-get -y install ttf-wqy-microhei \  
&& ln /etc/fonts/conf.d/65-wqy-microhei.conf /etc/fonts/conf.d/69-language-
selector-zh-cn.conf  
  
# 设置时区  
ENV TZ "PRC"  
RUN echo "Asia/Shanghai" | tee /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata \  
&& apt-get upgrade --yes  
  
# 删除不必要的软件和Apt缓存包列表  
RUN apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Docker's supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Expose SSH port  
# EXPOSE 22  
# Run SSH server  
CMD ["/usr/bin/supervisord"]  
  

