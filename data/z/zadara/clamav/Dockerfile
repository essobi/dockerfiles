FROM ubuntu:trusty  
## inotify setup  
RUN apt-get update && apt-get install -y inotify-tools  
  
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
&& apt-get install -y clamav-daemon clamav-freshclam \  
&& freshclam  
  
## Cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## Entrypoint files  
COPY ./clamav_daemon.sh /clamav_daemon.sh  
COPY ./inotify_monitor.sh /inotify_monitor.sh  
COPY ./ssh_server.sh /ssh_server.sh  
COPY ./start.sh start.sh  
RUN chmod +x /clamav_daemon.sh  
RUN chmod +x /inotify_monitor.sh  
RUN chmod +x /inotify_monitor.sh  
RUN chmod +x /start.sh  
  
CMD /start.sh

