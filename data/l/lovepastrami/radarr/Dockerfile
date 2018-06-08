FROM ubuntu  
  
RUN apt-get update -y && apt-get install -y wget libmono-cil-dev curl
mediainfo  
RUN wget
https://github.com/Radarr/Radarr/releases/download/v0.2.0.778/Radarr.develop.0.2.0.778.linux.tar.gz  
RUN tar zxvf Radarr.develop.0.2.0.778.linux.tar.gz  
RUN apt-get autoremove -y && apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 7878  
CMD /usr/bin/mono --debug /Radarr/Radarr.exe -nobrowser  

