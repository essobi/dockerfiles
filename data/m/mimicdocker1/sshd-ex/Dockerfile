From ubuntu  
  
MAINTAINER kent wu <kwu@suse.com>  
  
#ENV https_proxy "http://16.85.88.10:8080"  
#ENV http_proxy "http://16.85.88.10:8080"  
#ENV no_proxy "localhost, 127.0.0.1"  
ENV foo "bar"  
RUN apt-get update && apt-get install -y openssh-server vim iputils-ping  
RUN mkdir -p /var/run/sshd  
RUN echo 'root:demo' | chpasswd  
ADD sshd_config /et/ssh/sshd_config  
  
CMD /usr/sbin/sshd -D  
#CMD /bin/bash  

