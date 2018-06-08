FROM ubuntu:vivid  
MAINTAINER "Watermark Dev Team<dev@watermark.org>"  
EXPOSE 514 514/udp  
  
RUN apt-get update -y -q && \  
apt-get install -y rsyslog rsyslog-gnutls && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD ./logentries.all.crt /etc/logentries.all.crt  
ADD ./rsyslog.conf /etc/rsyslog.conf  
ADD ./run.sh /run.sh  
  
RUN chmod 755 /run.sh  
  
ENTRYPOINT [ "/run.sh" ]  

