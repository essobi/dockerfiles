FROM alpine  
  
MAINTAINER Frederic Darmstädter <docker@darmstaedter.org>  
  
ENV CLONE_FROM https://github.com/darmstaedter/welcome-project.git  
ENV CLONE_TO /usr/share/nginx  
ENV ADD_KNOWN_HOSTS github.com bitbucket.org  
ENV BRANCH master  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache bash git openssh-client && \  
mkdir /root/.ssh && \  
ssh-keyscan $ADD_KNOWN_HOSTS >> /root/.ssh/known_hosts && \  
mkdir -p $CLONE_TO/html/html && \  
rm -r $CLONE_TO/*  
  
CMD ssh-agent bash -c 'ssh-add /root/.ssh/id_rsa; git clone --single-branch
--branch $BRANCH $CLONE_FROM $CLONE_TO'  

