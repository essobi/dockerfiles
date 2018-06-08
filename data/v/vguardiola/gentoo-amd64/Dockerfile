FROM busybox  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
ADD build.sh /  
ADD localepurge.sh /  
ADD localelist /  
RUN /build.sh amd64 x86_64  
RUN sed -e 's/#rc_sys=""/rc_sys="lxc"/g' -i /etc/rc.conf  
RUN echo 'UTC' > /etc/timezone  

