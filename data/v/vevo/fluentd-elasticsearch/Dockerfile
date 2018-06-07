FROM debian:latest  
  
MAINTAINER Jestin Woods "jestin.woods@vevo.com"  
EXPOSE 24220  
RUN ulimit -n 65536  
ENV DEBIAN_FRONTEND noninteractive  
COPY build.sh /tmp/build.sh  
RUN /tmp/build.sh  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
  
ENTRYPOINT [ "td-agent" ]  

