FROM ubuntu:trusty  
MAINTAINER Borja Burgos <borja@tutum.co>, Mia Iversen <mia@chillfox.com>, Kun
Ran <kun@youdar.net>  
  
RUN apt-get update && apt-get install -y wget unzip axel mysql-client git  
  
ENV QSHELL_VERSION v1.7.2  
ENV QSHELL_ARCHiTECTURE linux_amd64  
ENV PATHS_TO_BACKUP /paths/to/backup  
ENV BACKUP_PREFIX dockup  
ENV RESTORE false  
  
RUN wget http://devtools.qiniu.com/qshell-$QSHELL_VERSION.zip \  
&& unzip qshell-$QSHELL_VERSION.zip -d /tmp/qshell \  
&& cp /tmp/qshell/qshell_$QSHELL_ARCHiTECTURE /usr/bin/qshell  
  
ADD backup.sh /backup.sh  
ADD restore.sh /restore.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
CMD ["/run.sh"]  

