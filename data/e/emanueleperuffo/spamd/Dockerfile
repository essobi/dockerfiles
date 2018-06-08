FROM emanueleperuffo/baseimage-debian:latest  
MAINTAINER Emanuele Peruffo <info@emanueleperuffo.com>  
  
ENV HOME /root  
ADD . /build  
  
ENV SPAMD_MAX_CHILDREN 5  
RUN /build/prepare.sh && \  
/build/services.sh && \  
/build/cleanup.sh  
  
EXPOSE 783  
CMD ["/sbin/my_init"]

