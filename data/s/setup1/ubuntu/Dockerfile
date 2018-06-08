FROM ubuntu:16.04  
MAINTAINER setup1  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y openssh-server  
RUN echo 'root:32886/rzw' |chpasswd  
RUN mkdir /var/run/sshd  
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.b  
RUN echo 'PermitRootLogin yes' > /etc/ssh/sshd_config  
  
RUN apt-get install -y python-pip  
RUN pip install shadowsocks  
  
#RUN wget https://raw.githubusercontent.com/setupre/ubuntu/master/media/run.sh  
EXPOSE 22  
EXPOSE 201  
ENTRYPOINT ssserver -p 201 -k 32886/rzw -m bf-cfb -d start && /usr/sbin/sshd
-D  
#CMD ["~/run.sh","-D"]  

