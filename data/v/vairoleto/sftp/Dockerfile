From ubuntu:trusty  
  
EXPOSE 22  
COPY utils /  
RUN apt-get update \  
&& apt-get -y install openssh-server \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod +x /scripts/* \  
&& mkdir /var/run/sshd  
CMD ["/usr/sbin/sshd", "-D"]  
#testing git  

