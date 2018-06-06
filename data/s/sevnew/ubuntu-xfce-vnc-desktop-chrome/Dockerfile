FROM ubuntu:14.04.3  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y  
RUN apt-get install -y supervisor wget \  
xfce4 xfce4-goodies x11vnc xvfb \  
gconf-service libnspr4 libnss3 fonts-liberation \  
libappindicator1 libcurl3 fonts-wqy-microhei  
  
# download google chrome and install  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome*.deb  
RUN apt-get install -f  
  
RUN apt-get autoclean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
ADD startup.sh ./  
ADD supervisord.conf ./  
  
# prepare chrome extension to install  
ADD kcoilljlnfjahoofolooodhmgojcfnpo.json /opt/google/chrome/extensions/  
  
# develop version chrome extension  
#COPY ext ./ext  
COPY xfce4 ./.config/xfce4  
  
EXPOSE 5900  
ENTRYPOINT ["./startup.sh"]  

