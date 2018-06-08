FROM alpine:latest  
  
ADD ./volumes/start.sh /etc/start.sh  
ADD ./volumes/supervisord.conf /etc/supervisord.conf  
ADD ./volumes/id_rsa /home/nagios/.ssh/id_rsa  
ADD ./volumes/id_rsa /root/.ssh/id_rsa  
ADD ./volumes/nrpe.cfg /etc/nagios/nrpe.cfg  
ADD ./volumes/check_example.sh /etc/nagios/check_example.sh  
  
RUN adduser nagios -S -h /home/nagios -s /bin/sh -D && \  
chown nagios /home/nagios/.ssh/* && \  
chown nagios /home/nagios/.ssh/ && \  
chmod 600 /root/.ssh/id_rsa && \  
chmod 600 /home/nagios/.ssh/id_rsa && \  
apk add --update sudo openssh-client nrpe curl supervisor py-yaml && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 5666  
WORKDIR /etc/nagios  
CMD ["/etc/start.sh"]  

