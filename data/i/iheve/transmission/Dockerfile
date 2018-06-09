FROM debian:wheezy  
MAINTAINER thibaut.coutelou@d2-si.eu  
  
#Install an ssh server and supervisord  
RUN apt-get -qq update  
RUN apt-get -qqy install openssh-server supervisor  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
EXPOSE 22  
#Install transmission  
RUN apt-get -qqy install transmission-daemon  
  
#Install nginx  
RUN apt-get -qqy install nginx  
EXPOSE 80  
#Configure supervisord  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#Configure transmission  
ADD settings.json /etc/transmission-daemon/  
RUN mkdir -p /dl  
EXPOSE 51413  
#Configure nginx  
ADD sites-enabled/ /etc/nginx/sites-enabled/  
ADD .htpasswd /  
  
#set root password  
#RUN mkdir -p /root/.ssh  
#ADD id_rsa.pub /root/.ssh/  
RUN echo "root:changeme" | chpasswd  
  
ADD entry.sh /root/entry.sh  
#CMD ["/usr/bin/supervisord"]  
CMD ["/root/entry.sh"]  

