FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV XYZ 1024x768x24  
ENV TZ "America/Los_Angeles"  
ENV VNC_PW "vncpassword"  
ENV DISPLAY :0  
RUN apt-get update -y && apt-get install -qqy --no-install-recommends wget
curl supervisor  
RUN apt-get -qqy --no-install-recommends install \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
language-pack-zh-hans \  
ttf-wqy-microhei  
  
RUN apt-get -y install xvfb x11vnc fluxbox xdotool ca-certificates && \  
mkdir ~/.vnc && \  
touch ~/.vnc/passwd  
RUN x11vnc -storepasswd $VNC_PW ~/.vnc/passwd  
  
RUN apt-get upgrade --yes && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY myrun /usr/bin/myrun  
RUN chmod +x /usr/bin/myrun  
  
EXPOSE 5900  
CMD ["/usr/bin/supervisord"]  

