FROM alpine:3.5  
  
MAINTAINER Gerónimo Afonso <geronimo.afonso@mikroways.net>  
  
RUN apk --update add --no-cache openssh openssh-sftp-server \  
&& sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \  
&& rm -rf /var/cache/apk/*  
  
RUN sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config \  
&& sed -ri 's&Subsystem sftp /usr/lib/ssh/sftp-server&#Subsystem sftp
/usr/lib/ssh/sftp-server&g' /etc/ssh/sshd_config \  
&& sed -ri 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey
\/etc\/ssh\/ssh_host_key/g' /etc/ssh/sshd_config \  
&& sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey
\/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config \  
&& sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey
\/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config \  
&& sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey
\/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config \  
&& sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey
\/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config \  
&& echo "#Config-sftp" >> /etc/ssh/sshd_config  
  
RUN /usr/bin/ssh-keygen -A  
  
COPY entrypoint.sh /init.sh  
  
EXPOSE 22  
  
ENTRYPOINT /init.sh  

