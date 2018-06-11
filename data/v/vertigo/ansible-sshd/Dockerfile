FROM vertigo/tiny-sshd:alpine  
  
LABEL maintainer andre@vertigo.com.br  
  
RUN apk --update add ansible sshpass curl  
# create ssh config for user  
RUN mkdir -p /home/user/.ssh && \  
echo "Host *\n StrictHostKeyChecking no\n UserKnownHostsFile=/dev/null" >
/home/user/.ssh/config  
  

