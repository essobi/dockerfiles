FROM debian:wheezy  
MAINTAINER thibaut.coutelou@d2-si.eu  
  
#Install an ssh server and supervisord  
RUN apt-get -qq update  
RUN apt-get -qqy install openssh-server supervisor  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
EXPOSE 22  
#Install serf  
RUN apt-get -qqy install wget ca-certificates  
RUN apt-get -qqy install unzip  
RUN wget https://dl.bintray.com/mitchellh/serf/0.6.3_linux_amd64.zip -O
/tmp/serf.zip  
RUN unzip /tmp/serf.zip -d /usr/local/bin  
RUN rm -f /tmp/serf.zip  
RUN mkdir -p /etc/serf  
EXPOSE 7946  
EXPOSE 80  
#Configure supervisord  
ADD bundle/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#Configure serf  
ADD bundle/serf-config /etc/serf  
  
#Default service name  
ENV SERVICE_NAME example.com  
#Disable SSH by default  
ENV SSH false  
  
ADD bundle/entry.sh /root/entry.sh  
CMD ["/root/entry.sh"]  

