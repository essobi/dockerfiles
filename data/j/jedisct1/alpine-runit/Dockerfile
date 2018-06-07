FROM alpine:latest  
  
ADD start_runit /sbin/  
RUN mkdir /etc/container_environment &&\  
chmod a+x /sbin/start_runit && mkdir /etc/service && mkdir /etc/runit_init.d
&& \  
apk --update upgrade && apk add bash util-linux coreutils findutils grep runit
&& rm -rf /var/cache/apk/*  
  
CMD ["/sbin/start_runit"]  

