FROM anapsix/alpine-java:8_server-jre_unlimited  
  
MAINTAINER Ken Huang <ken@wetech.io>  
RUN apk --update add supervisor  
  
RUN rm -rf /var/cache/apk/*  
  
WORKDIR /projects  
  
COPY run.sh /run.sh  
RUN chmod 755 /*.sh  
  
COPY etc/supervisord.conf /etc/supervisord.conf  
  
ENTRYPOINT ["/run.sh"]

