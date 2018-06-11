#  
# Official dind with sshd  
#  
FROM docker:stable-dind  
  
LABEL maintainer andre@vertigo.com.br  
  
RUN apk --update add openssh python sudo shadow py-pip curl && \  
/usr/bin/ssh-keygen -A && \  
pip install --upgrade docker docker-compose  
ADD src/*.sh /opt/  
RUN adduser -D -u 5001 user && \  
groupadd docker && \  
usermod -G wheel user && \  
usermod -G docker user && \  
echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
sed -i s/^#PasswordAuthentication.*/PasswordAuthentication\ yes/
/etc/ssh/sshd_config && \  
chmod +x /opt/*.sh  
  
EXPOSE 22  
# entrypoint inherited from dind, cmd execs after  
ENTRYPOINT ["/opt/startsshd.sh"]  
  

