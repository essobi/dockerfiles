FROM ubuntu:15.04  
MAINTAINER Nick Groenen <nick@groenen.me>  
  
ENV ERR_PYTHON_VERSION 2  
ENV ERR_PACKAGE https://github.com/gbin/err/archive/master.zip  
  
COPY scripts/runas.sh /usr/local/sbin/runas  
  
COPY provisioners/base.sh /provision.sh  
RUN /provision.sh && rm /provision.sh  
  
COPY provisioners/app.sh /provision.sh  
RUN /provision.sh && rm /provision.sh  
  
COPY scripts/start.sh /bin/start.sh  
ENTRYPOINT ["/bin/start.sh"]  
  
VOLUME ["/err/data/"]  

