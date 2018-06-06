FROM lsiobase/alpine  
MAINTAINER rix1337  
  
# install autossh and sshpass and required packages  
RUN apk update && apk add --no-cache openssh sshpass  
RUN apk add autossh --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/community/  
  
# add local files  
COPY root/ /  
  
#Port  
EXPOSE 10101  

