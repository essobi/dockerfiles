FROM debian:wheezy  
MAINTAINER Glenn ROLLAND, <glenux@glenux.net>  
RUN apt-get update  
RUN apt-get install -y openssh-server  
RUN service ssh start ; sleep 1  
RUN service ssh stop  
RUN echo "root:docker" | chpasswd  
RUN apt-get install -y supervisor bindfs  
RUN service supervisor stop  
  
EXPOSE 22  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD supervisor-ssh.conf /etc/supervisor/conf.d/ssh.conf  
  
CMD /usr/bin/supervisord  

