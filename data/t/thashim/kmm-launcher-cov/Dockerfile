#Baseline  
FROM ubuntu:14.04  
  
MAINTAINER Tatsunori Hashimoto <thashim@mit.edu>  
  
RUN sudo apt-get update  
RUN sudo apt-get -q -y install r-base openssh-client python-pip  
RUN sudo pip install awscli  
RUN sudo apt-get install samtools parallel  
  
RUN mkdir /kmm  
  
ADD run.onestrand.r /kmm/run.onestrand.r  
ADD run.cluster.onestrand.r /kmm/run.cluster.onestrand.r  
ADD standalone.template.txt /kmm/standalone.template.txt  
ADD user-data.txt /kmm/user-data.txt  
  
RUN chmod +x /kmm/run.onestrand.r  
RUN chmod +x /kmm/run.cluster.onestrand.r  
RUN chmod -R 777 /kmm  
  
  
#launch me with  
#docker build --no-cache=t -t thashim/kmm-launcher2 .  
#docker run --rm -t -v /cluster:/cluster -i thashim/kmm-launcher /bin/bash  
#docker run --rm -w `pwd` -v /cluster:/cluster -i thashim/kmm-launcher2
/kmm/run.onestrand.r example/covbinom.list /cluster/ec2/auth.txt  
#args=c('/cluster/thashim/docker/kmm-
launcher/example/covbinom.list','/cluster/ec2/auth.txt')  

