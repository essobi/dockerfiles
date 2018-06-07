FROM frolvlad/alpine-glibc:alpine-3.6  
MAINTAINER Steve Hibit <sdhibit@gmail.com>  
  
# Install runit & helpful packages  
RUN apk --update upgrade \  
&& apk --no-cache add \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community \  
curl \  
runit \  
su-exec  
  
ADD start_runit /sbin/  
  
RUN chmod a+x /sbin/start_runit \  
&& mkdir -p /etc/container_environment \  
/etc/service \  
/etc/runit_init.d  
  
CMD ["/sbin/start_runit"]  

