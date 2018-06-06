FROM ubuntu:14.04  
MAINTAINER Kevin Krummenauer <kevin@whiledo.de>  
#Originally from MAINTAINER Sven Dowideit <SvenDowideit@docker.com>
https://docs.docker.com/engine/examples/running_ssh_service/  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
ADD resources /data/resources  
ADD https://raw.githubusercontent.com/kekru/linux-utils/master/shell-forward-
via-files/server /data/resources/shellforward/server  
ADD https://raw.githubusercontent.com/kekru/linux-utils/master/shell-forward-
via-files/client /data/resources/shellforward/client  
RUN chmod 751 /data/resources/entrypoint.sh  
  
ENV SSHUSER="root" \  
SSHPASSWD="root" \  
SHELLFORWARD="no"  
EXPOSE 22  
CMD ["/data/resources/entrypoint.sh"]  

