FROM ubuntu:16.04  
RUN apt-get update -qq  
RUN apt-get install -y git make gcc ruby  
ADD ci-git-diff-notification-service.rb .  
ADD aha ./aha/  
WORKDIR "aha"  
RUN make  
RUN make install

