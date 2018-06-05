FROM daewood/abase  
  
MAINTAINER daewood <daewood@qq.com>  
  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk --update add mongodb mongodb-tools \  
&& rm -rf /var/cache/apk/* \  
&& rm /usr/bin/mongosniff /usr/bin/mongoperf  
  
COPY rootfs/ /  
  
ENTRYPOINT ["/init"]  
CMD []  
  
EXPOSE 27017  
VOLUME ["/data/db"]  

