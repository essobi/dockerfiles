FROM ubuntu:trusty  
  
## SSH setup  
RUN echo 'root:zadara' | chpasswd  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& sed -i 's/PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config \  
&& echo 'UseDNS no' >> /etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
EXPOSE 22  
## Clamav setup  
RUN apt-get update \  
&& apt-get install -y clamav-daemon clamav-freshclam curl \  
&& freshclam  
  
# Add jq  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O
/usr/local/bin/jq && \  
chmod +x /usr/local/bin/jq  
  
## Cleanup  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## Entrypoint files  
#COPY ./clamav_daemon.sh /clamav_daemon.sh  
#COPY ./queue_process.sh /queue_process.sh  
#COPY ./find_changes.sh /find_changes.sh  
#COPY ./ssh_server.sh /ssh_server.sh  
#COPY ./start.sh /start.sh  
COPY ./*.sh /  
RUN chmod +x /clamav_daemon.sh \  
/queue_process.sh \  
/find_changes.sh \  
/ssh_server.sh \  
/start.sh  
  
CMD /start.sh  

