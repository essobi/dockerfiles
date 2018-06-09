FROM phusion/baseimage:0.9.15  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV TERM screen  
MAINTAINER x0nic <nathan@globalphobia.com>  
  
ENV VERSION 15.0  
ADD http://downloads.sourceforge.net/project/nzbget/nzbget-
stable/$VERSION/nzbget-$VERSION.tar.gz /tmp/nzbget.tar.gz  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
COPY install.sh /tmp/  
RUN chmod +x /tmp/install.sh  
RUN /tmp/install.sh  
  
VOLUME /config  
VOLUME /downloads  
  
EXPOSE 6789  
# Add config.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
COPY config.sh /etc/my_init.d/config.sh  
  
# Add nzbget to runit  
RUN mkdir /etc/service/nzbget  
COPY nzbget.sh /etc/service/nzbget/run  
  
# Tail nzblog and make visible to docker  
RUN mkdir /etc/service/tail  
COPY tail.sh /etc/service/tail/run  
  
RUN chmod +x /etc/service/*/run /etc/my_init.d/*  

