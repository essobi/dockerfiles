FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get -y install openssh-client  
CMD ssh-keygen -q -t rsa -N '' -f /tmp/rsa-key && cat /tmp/rsa-key.pub && cat
/tmp/rsa-key  

