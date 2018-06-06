FROM jacekkow/kodi  
  
RUN echo "Europe/Warsaw" > /etc/timezone \  
&& rm -f /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  

