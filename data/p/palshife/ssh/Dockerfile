FROM ubuntu:wily  
RUN apt-get update && apt-get install -y openssh-server daemontools  
RUN mkdir -p /etc/myservices/sshd /var/run/sshd  
RUN echo "#!/bin/bash\nexec /usr/sbin/sshd" > /etc/myservices/sshd/run  
RUN chmod +x /etc/myservices/sshd/run  
EXPOSE 22  
ENTRYPOINT ["/usr/bin/svscan", "/etc/myservices/"]  

