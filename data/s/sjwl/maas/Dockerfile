FROM solita/ubuntu-systemd:16.04  
  
ENV container docker  
  
RUN apt-get -qq update && \  
apt-get -y install sudo  
  
#install rsyslog  
RUN apt-get install -y rsyslog  
RUN systemctl enable rsyslog.service  
  
#install maas  
RUN systemctl enable rsyslog.service && \  
service rsyslog restart && \  
apt-get install -y maas && \  
maas createadmin \--username=root \--password=welcome1 \--email=foo@foo.com

