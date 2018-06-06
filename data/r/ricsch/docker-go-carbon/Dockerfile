FROM phusion/baseimage:latest  
  
#ENV NODE_NAME cache  
ENV LOCAL_DATA_DIR /opt/graphite/storage/whisper/  
#ENV MAX_CACHE_SIZE inf  
#ENV MAX_UPDATES_PER_SECOND 1000  
#ENV MAX_CREATES_PER_MINUTE inf  
#ENV LOG_UPDATES False  
#ENV LINE_RECEIVER_INTERFACE 0.0.0.0  
#ENV PICKLE_RECEIVER_INTERFACE 0.0.0.0  
#ENV CACHE_QUERY_INTERFACE 0.0.0.0  
#ENV LINE_RECEIVER_PORT 2003  
#ENV PICKLE_RECEIVER_PORT 2004  
#ENV CACHE_QUERY_PORT 7002  
# System update/upgrade and tool install  
RUN apt-get update  
RUN apt-get install -y git golang make wget  
RUN apt-get upgrade -y  
  
# Download and install go carbon  
RUN wget https://github.com/lomik/go-carbon/releases/download/v0.7-beta4/go-
carbon_0.7-beta4_amd64.deb  
RUN dpkg -i go-carbon_0.7-beta4_amd64.deb  
  
VOLUME /opt/graphite/storage  
  
ADD ./config /opt/graphite/config/  
  
RUN mkdir /etc/service/go-carbon  
ADD start.sh /etc/service/go-carbon/run  
  
EXPOSE 2003 2004 7002  
CMD ["/sbin/my_init"]  

