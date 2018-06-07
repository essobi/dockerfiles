FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get -y install curl wget  
RUN curl -sL https://minergate.com/download/deb-cli -o deb-cli && dpkg -i deb-
cli && rm -f deb-cli  
CMD nice -18 minergate-cli -user kawazzz@gmail.com -xmr  

