FROM alpine  
MAINTAINER Randy Ramos <rramos1295 \at\ gmail \dot\ com>  
  
ENV SSH_USER=sftp  
ENV SSH_PASS=DockerPassSFTP  
ENV ROOT_PASS=RootPassSFTP  
  
RUN apk add --no-cache bash openssh shadow  
RUN ssh-keygen -A \  
&& useradd -m -s /bin/bash $SSH_USER \  
&& echo "$SSH_USER:$SSH_PASS" | chpasswd \  
&& echo -e "$ROOT_PASS\n$ROOT_PASS" | passwd  
  
ADD sshd_config /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

