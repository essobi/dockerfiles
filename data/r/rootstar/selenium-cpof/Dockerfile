FROM ubuntu:trusty  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
RUN apt-get -y update  
RUN apt-get install -y -q software-properties-common wget  
RUN add-apt-repository -y ppa:mozillateam/firefox-next  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get -y update  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
  
RUN apt-get install -y aptitude  
  
RUN wget -O - http://deb.opera.com/archive.key | apt-key add -  
RUN echo "deb http://deb.opera.com/opera/ stable non-free" >>
/etc/apt/sources.list.d/opera.list  
  
RUN apt-get update -y  
RUN aptitude update -y  
  
RUN mkdir -p /usr/share/desktop-directories  
RUN apt-get install -y -q firefox google-chrome-stable openjdk-7-jre-headless
make g++ curl nodejs git  
RUN yes "Yes" | aptitude install -y opera  
RUN apt-get install -y -q x11vnc xvfb xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic  
  
RUN useradd -d /home/user -m user  
RUN mkdir -p /home/user/chrome /home/user/firefox /home/user/opera
/home/user/phantom  
RUN chown -R user /home/user  
RUN chgrp -R user /home/user  
  
RUN npm install -g selenium-standalone@latest  
RUN npm install -g phantomjs  
RUN npm install -g angular-no-vnc  
  
RUN selenium-standalone install  
  
ENV screen_width 1360  
ENV screen_height 1020  
ENV screen_depth 24  
ENV vnc_ws_port 4999  
ENV vnc_password password  
ENV selenium_port 4444  
ENV DISPLAY_NUM 99  
ENV DISPLAY :${DISPLAY_NUM}.0  
ADD ./start.sh /root/  
  
ENTRYPOINT ["sh", "/root/start.sh"]  

