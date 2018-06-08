FROM docker:stable-dind  
  
RUN apk add --update alpine-sdk  
RUN apk add --update bash python python-dev py-pip build-base openssh jq rsync  
RUN apk add -U --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing
aufs-util  
RUN pip install docker-compose  
RUN pip install awscli  
RUN mkdir -p ~/.ssh/  
RUN echo -e "Host *\n StrictHostKeyChecking no\n UserKnownHostsFile=/dev/null"
> ~/.ssh/config  
  
COPY start.sh /etc/start.sh  
  
RUN chmod +x /etc/start.sh  
  
CMD /etc/start.sh  

