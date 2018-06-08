FROM debian:latest  
MAINTAINER Yann Hodique <hodiquey@vmware.com>  
ENV REFRESHED_AT 12/2/2014  
ENV ADDR ${1:-$FORWARD_ADDR}  
  
RUN apt-get update  
RUN apt-get install -y socat  
  
#ADD forward.sh /forward.sh  
# clean any temp files  
RUN apt-get autoclean  
RUN apt-get autoremove  
RUN apt-get clean  
RUN rm -rf /tmp/*  
  
EXPOSE 10000  
CMD socat TCP-LISTEN:10000,fork TCP:$ADDR  

