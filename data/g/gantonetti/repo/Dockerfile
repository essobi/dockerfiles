FROM debian  
MAINTAINER Gilles <gilles@docker.com>  
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade  
RUN apt-get -y install curl  
ENV HELLO 'hello world!'  
COPY README.md /tmp/  
COPY hello.sh /tmp/  
#ENTRYPOINT ["/tmp/hello.sh"]  
WORKDIR /home  

