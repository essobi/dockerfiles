# Dockerfile for building Ansible > 1.9 image for Alpine 3, with as few
additional software as possible.  
#  
# @see https://github.com/gliderlabs/docker-alpine/blob/master/docs/usage.md  
#  
# Version 1.0  
#  
# pull base image  
FROM alpine:3.6  
  
MAINTAINER Pincemail Sebastien <pincemail.sebastien@gmail.com>  
  
RUN echo "===> Installing sudo to emulate normal OS behavior..." && \  
apk --update add sudo && \  
\  
\  
echo "===> Adding Python runtime and dependencies..." && \  
apk --update add python py-pip openssl ca-certificates git && \  
apk --update add --virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi && \  
\  
\  
echo "===> Installing Ansible..." && \  
pip install ansible==2.4.0 && \  
\  
\  
echo "===> Installing handy tools (not absolutely required)..." && \  
apk --update add sshpass openssh-client rsync && \  
\  
\  
echo "===> Removing unacessary package..." && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/* && \  
\  
\  
echo "===> Adding hosts for convenience..." && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts && \  
\  
echo "===> Create user for deploy... " && \  
adduser -s /bin/sh -D deployer && mkdir /home/deployer/.ssh  
  
USER root  
COPY configuration/id_rsa /root/.ssh/id_rsa  
COPY configuration/known_hosts /root/.ssh/known_hosts  
COPY configuration/id_rsa /home/deployer/.ssh/id_rsa  
COPY configuration/known_hosts /home/deployer/.ssh/known_hosts  
  
RUN chmod 400 /root/.ssh/id_rsa && chown root /root/.ssh/id_rsa && \  
chmod 400 /home/deployer/.ssh/id_rsa && chown deployer
/home/deployer/.ssh/id_rsa  
#ssh-keyscan git.groupe.generali.fr >> /root/.ssh/known_hosts &&\  
#RUN git clone
ssh://git@git.groupe.generali.fr:7999/~b011KKj/ansible_deploy.git
/home/deployer/ansible-deploy  
# default command: display Ansible version  
CMD [ "ansible-playbook", "--version" ]  

