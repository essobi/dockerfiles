FROM node:alpine  
# container info  
LABEL maintainer fmakdemir  
LABEL description "This docker is aiming to be a phabricator drydock resource\  
container to be used on nodejs tests with harbormaster"  
  
# make required dirs  
RUN mkdir -p /var/drydock  
# setup working dir  
WORKDIR /var/drydock  
  
# install required utilities  
RUN apk update && apk add\  
openssh\  
git  
# setup keys  
RUN ssh-keygen -A  
  
COPY sshd_config ssh_config /etc/ssh/  
COPY start.sh /opt/start.sh  
COPY ssh /root/.ssh  
RUN chmod +x /opt/start.sh  
  
# COPY ssh_config /etc/ssh/ssh_config  
# expose port 22 to let phab connect to this container  
# NOTE: this is just exposed port check -p flag of docker run command  
EXPOSE 22  
# CMD ["echo", "I run"]  
# RUN /usr/sbin/sshd  
CMD ["/opt/start.sh"]  

