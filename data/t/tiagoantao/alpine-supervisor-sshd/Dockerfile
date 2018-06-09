FROM tiagoantao/alpine-base  
MAINTAINER Tiago Antao <tiagoantao@gmail.com>  
  
RUN apk update  
RUN apk add supervisor nss-pam-ldapd  
RUN apk add openssh bash  
RUN apk add zabbix-agent  
RUN apk add python3 wget  
  
#this machine cannot be run without adding a root key  
#(and server key should be changed also)  
#Explain prepare magic somewhere  
#Install Linking of configuration files and entrypoint  
RUN wget --no-check-certificate
https://raw.githubusercontent.com/tiagoantao/mutable_files/master/link_mutable_files.py
-O /sbin/link_mutable_files.py  
COPY copy/sbin/server_run.sh /sbin  
RUN chmod a+x /sbin/server_run.sh /sbin/link_mutable_files.py  
RUN mkdir /traverse  
RUN sed -i 's/Server=.*/Server=zabbix/' /etc/zabbix/zabbix_agentd.conf  
  
COPY copy/etc/supervisor.d/supervisor.ini /etc/supervisor.d/  
COPY copy/etc/supervisor.d/supervisor-sshd.ini /etc/supervisor.d/  
  
COPY copy/etc/ssh/sshd_config /etc/ssh/  
RUN ssh-keygen -A  
RUN mkdir /root/.ssh  
  
#EXPOSE 22  
CMD ["/sbin/server_run.sh"]  

