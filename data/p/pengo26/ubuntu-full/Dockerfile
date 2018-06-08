FROM ubuntu  
  
MAINTAINER İlter Engin KIZILGÜN <programyazar@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y inetutils-ping  
RUN apt-get install -y vim  
RUN apt-get install -y nginx  
RUN apt-get install -y python2.7  
RUN apt-get install -y python-pip  
RUN apt-get install -y curl  
RUN apt-get install -y netcat  
RUN apt-get install -y git  
RUN apt-get install -y openssh-server  
RUN apt-get install -y mysql-client  
RUN apt-get install -f -y  
RUN pip install --upgrade pip  
RUN pip install Flask  
RUN mkdir /var/run/sshd  
  
EXPOSE 22  
EXPOSE 80  
  
CMD ["/usr/sbin/sshd", "-D"]  
CMD ["nginx", "-g", "daemon off;"]  
  
  
ENTRYPOINT  service ssh start && service nginx start && /bin/bash  

