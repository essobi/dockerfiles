FROM alpine:3.4  
RUN apk --no-cache --update add git openssh  
  
RUN mkdir /root/.ssh/  
  
ADD known_hosts /root/.ssh/known_hosts  
ADD backup-jenkins.sh ./backup-jenkins.sh  
RUN chmod 700 ./backup-jenkins.sh  
  
ENTRYPOINT ["/bin/sh", "./backup-jenkins.sh"]  
  

