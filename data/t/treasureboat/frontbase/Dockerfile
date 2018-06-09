#  
# TreasureBoat.org  
# by daveeed  
#  
# Frontbase 5.2.14 on CentOS 6.6  
#  
# build : docker build -t treasureboat/frontbase:0.6 .  
# run : docker run -d -P -p 20020:20020 -p 30001:30001 --name tbFB5
treasureboat/frontbase:0.6  
FROM treasureboat/java:latest  
MAINTAINER treasureboat <programmingosx@mac.com & office@treasureboat.org>  
  
# download FrontBase  
RUN wget -q -O /tmp/FrontBase.rpm
'https://dl.dropboxusercontent.com/u/1548210/TB/Docker/FrontBase-5.2.14-CentOS-5.4-x86_64.rpm'  
  
# install FrontBase  
RUN rpm -i /tmp/FrontBase.rpm  
RUN rm -f /tmp/FrontBase.rpm  
  
# add boot script  
RUN printf '\n[program:frontbase]\n' >> /etc/supervisor/supervisord.conf  
RUN printf 'command = /usr/local/FrontBase/bin/FBExec\n' >>
/etc/supervisor/supervisord.conf  
  
# support for 5 fixed IP Databases for now  
# TODO find better solution  
EXPOSE 22 20020 30001 30002 30003 30004 30005  
# TODO expose Backup folder  
# VOLUME ["/usr/local/FrontBase/Backups"]  

