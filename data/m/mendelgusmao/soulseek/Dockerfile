FROM ubuntu:17.04  
MAINTAINER Mendelson Gusmão  
  
ENV DISPLAY :1  
ENV SOULSEEK_DL
"https://www.dropbox.com/s/7qh902qv2sxyp6p/SoulseekQt-2016-1-17-64bit.tgz?dl=1"  
RUN apt-get -yy update \  
&& apt-get -y install --no-install-recommends wget libx11-6 libx11-xcb1
libfontconfig1 supervisor xvfb x11vnc software-properties-common openbox xterm  
  
RUN addgroup soulseek \  
&& useradd -m -s /bin/bash -g soulseek soulseek  
WORKDIR /home/soulseek  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD menu.xml /etc/xdg/openbox/menu.xml  
ADD start /bin/start  
RUN wget -qO- "$SOULSEEK_DL" | tar xzvf - -C /usr/bin
--transform='s/.*/soulseek/'  
  
RUN apt-get -y remove --purge wget; \  
apt-get -y autoremove; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*  
  
USER soulseek  
EXPOSE 5900 2234 2235  
CMD ["/bin/start"]  

