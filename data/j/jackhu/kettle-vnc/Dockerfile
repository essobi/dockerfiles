FROM jackhu/docker-kettle:6.1  
MAINTAINER Jack Hu <hello@jackhu.top>  
  
# 无交互模式  
ENV DEBIAN_FRONTEND noninteractive  
# vnc 默认密码  
ENV VNC_PW "vncpassword"  
# 中文支持  
RUN locale-gen zh_CN.UTF-8 && \  
dpkg-reconfigure --frontend noninteractive locales  
ENV LANG zh_CN.UTF-8  
ENV LANGUAGE zh_CN:zh  
ENV LC_ALL zh_CN.UTF-8  
# 时区配置  
ENV TZ "Asia/Shanghai"  
RUN echo $TZ > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
# 安装supervisor, 桌面xfce4, 中文字体, 和vnc服务, 删除不必要的软件和Apt缓存包列表  
RUN apt-get update && \  
apt-get install -y --force-yes --no-install-recommends \  
supervisor \  
fonts-wqy-microhei ttf-wqy-zenhei \  
xfce4 xfce4-goodies \  
x11vnc xvfb && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
#配置VNC密码  
RUN mkdir ~/.vnc && \  
touch ~/.vnc/passwd && \  
x11vnc -storepasswd $VNC_PW ~/.vnc/passwd  
  
ADD startup.sh $PENTAHO_HOME/docker-entrypoint.d/  
ADD supervisord.conf /root/  
RUN chmod +x $PENTAHO_HOME/docker-entrypoint.d/startup.sh  
  
EXPOSE 5900

