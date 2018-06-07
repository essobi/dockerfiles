FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
dnsutils \  
iputils-ping \  
net-tools \  
openssh-server \  
traceroute \  
tcptraceroute \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY authorized_keys /root/.ssh/  
  
RUN mkdir /var/run/sshd \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
WORKDIR /  
COPY ssh.sh /  
EXPOSE 22  
CMD ["/ssh.sh"]  

