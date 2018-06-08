FROM jenkins:2.60.3  
  
USER root  
  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias
fr_FR.UTF-8 \  
&& echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
ENV LANG fr_FR.utf8  
  
USER jenkins  

