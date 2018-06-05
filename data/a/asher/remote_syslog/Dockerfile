FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -L -O
https://github.com/papertrail/remote_syslog2/releases/download/v0.13/remote_syslog_linux_amd64.tar.gz  
RUN tar zxvf remote_syslog_linux_amd64.tar.gz  
RUN cp remote_syslog/remote_syslog /usr/local/bin  
RUN rm -r remote_syslog  
  
CMD ["remote_syslog"]  

