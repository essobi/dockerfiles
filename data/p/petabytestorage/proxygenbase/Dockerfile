FROM ubuntu:17.10  
# build proxygen version 2018-02-26  
MAINTAINER rudi@petabytestorage.com  
RUN apt update -y  
ENV LD_LIBRARY_PATH /usr/local/lib  
RUN apt install -y libboost-all-dev wget sudo build-essential libmysqlcppconn-
dev  
WORKDIR /root  
RUN wget https://github.com/facebook/proxygen/archive/v2018.02.26.00.tar.gz  
RUN tar xvfz v2018.02.26.00.tar.gz  
WORKDIR /root/proxygen-2018.02.26.00  
RUN cd proxygen && head --lines=-7 deps.sh >d2.sh && cat d2.sh >deps.sh && rm
d2.sh && ./deps.sh  
WORKDIR /root  

