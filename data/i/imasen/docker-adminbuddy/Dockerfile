FROM alpine  
  
MAINTAINER https://github.com/imasen  
  
RUN apk add --update git vim bash openssh-client rsync curl subversion py-pip
docker docker-vim docker-bash-completion ansible  
  
RUN pip install awscli  
  
ENTRYPOINT /bin/bash  

