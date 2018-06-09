FROM phusion/baseimage:0.9.15  
MAINTAINER Guilhem Berna <guilhem.berna@gmail.com>  
  
RUN apt-get update && apt-get install -qy rsync ksh pwgen  
  
#creating user with generated password  
RUN useradd -u 1111 -g backup -m bkp  
RUN echo "bkp:$(pwgen -s -1 30)" | chpasswd  
  
#Adding exploitation scripts  
ADD scriptsexploit.tar /  
RUN chown -R bkp:backup /appli  
RUN chmod -R 740 /appli  
RUN /appli/exploit/prg/outils/install_tousprofile.ksh  
  
#creating exploitation backup, log and tmp directories  
RUN mkdir -p /var/backup/db  
RUN mkdir -p /var/log/exploit  
RUN mkdir -p /var/tmp_app/exploit  
RUN chown -R bkp:backup /var/backup /var/log/exploit /var/tmp_app/exploit  
  
#adding the public key  
USER bkp  
COPY backuppc.pub /tmp/backuppc.pub  
RUN mkdir -p /home/bkp/.ssh  
RUN cat /tmp/backuppc.pub >> /home/bkp/.ssh/authorized_keys  
  
#restricting access to user bkp  
USER root  
RUN echo "bkp ALL=NOPASSWD: /usr/bin/rsync --server --sender *" >>
/etc/sudoers  
RUN sed -i "s/.*PasswordAuthentication.*/PasswordAuthentication no/g"
/etc/ssh/sshd_config  
  
#cleanup  
RUN rm -f /tmp/backuppc.pub  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 22  

