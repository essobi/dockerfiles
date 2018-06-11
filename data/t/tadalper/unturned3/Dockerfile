FROM ubuntu:xenial  
  
EXPOSE 27016/udp  
EXPOSE 27017/udp  
VOLUME ["/home/steamcmd"]  
VOLUME ["/home/unturned"]  
  
RUN useradd -ms /bin/bash unt  
RUN apt-get update && apt-get install -y apt-utils cron ca-certificates
lib32gcc1 unzip net-tools lib32stdc++6 lib32z1 lib32z1-dev curl wget screen
tmux  
  
RUN mkdir -p /home/steamcmd && curl -s
http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -v -C
/home/steamcmd -zx  
RUN mkdir -p /home/unturned  
  
ADD start.sh /home/unturned/start.sh  
RUN chmod a+x /home/unturned/start.sh  
RUN (crontab -l ; echo "* * * * * /home/unturned/start.sh") | sort - | uniq -
| crontab -  
  
ADD update.sh /home/unturned/update.sh  
RUN chmod a+x /home/unturned/update.sh  
RUN (crontab -l ; echo "@daily /home/unturned/update.sh") | sort - | uniq - |
crontab -  
  
ADD credentials/STEAM_USERNAME /root/.steam_user  
ADD credentials/STEAM_PASSWORD /root/.steam_pass  
  
ONBUILD USER root  
ONBUILD run /home/unturned/update.sh  

