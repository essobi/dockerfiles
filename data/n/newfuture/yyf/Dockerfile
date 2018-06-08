FROM newfuture/yaf:latest  
MAINTAINER New Future <docker@newfuture.cc>  
LABEL Name="YYF-docker-demo" Description="docker image for YYF demo"  
# Environments  
ENV PORT=80 \  
TIMEZONE=UTC \  
DISPLAY_ERROR=1 \  
STARTUP_ERROR=1 \  
ASSERTIONS=1 \  
WORK_DIR=/yyf/  
  
WORKDIR $WORK_DIR  
  
# download  
ADD "https://github.com/YunYinORG/YYF/archive/master.tar.gz" /yaf/  
RUN rm -rf /var/cache/apk/* \  
/var/tmp/* \  
/tmp/* \  
/etc/ssl/certs/*.pem \  
/etc/ssl/certs/*.0 \  
/usr/share/ca-certificates/mozilla/* \  
/usr/share/man/* \  
/usr/include/*  
  
  
COPY ./run.sh /run.sh  
  
CMD /run.sh  

