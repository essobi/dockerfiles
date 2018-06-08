#onionscan container for general purpose:  
#info @ https://github.com/s-rah/onionscan  
FROM golang:1.7  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
#install updates, some packages and do cleanup:  
RUN apt-get update && apt-get upgrade -y\  
&& apt-get install tor torsocks -y\  
&& go get github.com/s-rah/onionscan\  
&& go install github.com/s-rah/onionscan  

