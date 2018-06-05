FROM ubuntu:14.04  
MAINTAINER Nathan Johnson <docker@njohnson.me>  
ENV REFRESHED_AT 2016-01-18  
RUN apt-get update \  
&& apt-get install -y socat  
  
ADD forward.sh /forward.sh  
  
ENTRYPOINT [ "/forward.sh" ]  

