FROM ubuntu:16.04  
MAINTAINER Haixin Lee <docker@lihaixin.name>  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV XYZ 1024x768x16  
ENV TZ "Asia/Shanghai"  
ENV VNC_PW "vncpassword"  
ENV DISPLAY :0  
ENV PURL 8.8.8.8  
ENV PPORT 6000  
ENV PPASSWORD pass123  
  
  
#升级仓库，安装基本网络包  
RUN apt-get update -y && \  
apt-get install -qqy --no-install-recommends \  
gettext-base wget curl iputils-ping iproute2 mtr apt-utils \  
vim net-tools supervisor  
  
# 安装基本字体  
RUN apt-get -qqy --no-install-recommends install \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
language-pack-zh-hans \  
ttf-wqy-microhei  
  
#升级系统，安装必要的包，配置VNC密码  
RUN apt-get -y install xvfb x11vnc fluxbox xdotool git git-core ca-
certificates && \  
mkdir ~/.vnc && \  
touch ~/.vnc/passwd  
RUN x11vnc -storepasswd $VNC_PW ~/.vnc/passwd  
  
# 克隆 noVNC和设置novnc首页  
RUN git clone \--recursive https://github.com/kanaka/noVNC.git /opt/novnc && \  
git clone \--recursive https://github.com/kanaka/websockify.git
/opt/novnc/utils/websockify && \  
ln -s /opt/novnc/vnc.html /opt/novnc/index.html  
  
#安装chromium 和tsocks  
RUN apt-get install -y --no-install-recommends chromium-browser tsocks  
  
#安装shadowsocks  
RUN apt-get install -y python-pip python-m2crypto && \  
pip install --upgrade pip && \  
pip install shadowsocks && \  
pip install --upgrade tzupdate  
  
# 升级到最新版本 删除不必要的软件和Apt缓存包列表  
RUN apt-get upgrade --yes && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# 容器里超级进程管理和配置文件  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY tsocks.conf /etc/tsocks.conf  
COPY myrun /usr/bin/myrun  
RUN chmod +x /usr/bin/myrun  
  
# 开放VNC端口和noVNC端口  
# EXPOSE 5900  
EXPOSE 8787  
# 运行各种Service  
CMD ["/usr/bin/supervisord"]  
  

