FROM ubuntu:14.04.3  
MAINTAINER Fang Zhihao <zhfang@dataman-inc.com>  
  
#COPY sources.list /etc/apt/sources.list  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /home/ubuntu  
  
# built-in packages  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends software-properties-
common curl \  
&& sudo sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >>
/etc/apt/sources.list.d/arc-theme.list" \  
&& curl -SL
http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key
| sudo apt-key add - \  
&& add-apt-repository ppa:fcwu-tw/ppa \  
&& apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends \  
supervisor \  
openssh-server pwgen sudo \  
net-tools \  
lxde x11vnc xvfb \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
firefox git wget vim telnet openjdk-7-jdk \  
fonts-wqy-microhei \  
language-pack-zh-hant language-pack-gnome-zh-hant firefox-locale-zh-hant \  
nginx \  
python-pip python-dev build-essential \  
mesa-utils libgl1-mesa-dri \  
gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme
\  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD web /web/  
RUN pip install setuptools wheel && pip install -r /web/requirements.txt  
  
# tini for subreap  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
RUN chmod +x /bin/tini  
  
RUN apt-get update \  
&& easy_install robotframework \  
&& easy_install robotframework-selenium2library \  
&& cd /usr/local/bin \  
&& wget
https://github.com/mozilla/geckodriver/releases/download/v0.10.0/geckodriver-v0.10.0-linux64.tar.gz
\  
&& tar -xzvf geckodriver-v0.10.0-linux64.tar.gz \  
&& rm -rf geckodriver-v0.10.0-linux64.tar.gz \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DISPLAY=localhost:1  
ADD noVNC /noVNC/  
ADD nginx.conf /etc/nginx/sites-enabled/default  
ADD startup.sh /  
ADD supervisord.conf /etc/supervisor/conf.d/  
ADD doro-lxde-wallpapers /usr/share/doro-lxde-wallpapers/  
ADD gtkrc-2.0 /home/ubuntu/.gtkrc-2.0  
  
EXPOSE 6080 22  
WORKDIR /root  
ENTRYPOINT ["/startup.sh"]  

