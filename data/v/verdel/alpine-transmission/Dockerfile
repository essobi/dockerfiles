FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV TRANSMISSION_CONF_DIR /etc/transmission  
  
# Copy init scripts  
COPY rootfs /  
  
# Install transmission and pushnotify  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
apk --update add \  
transmission-daemon@edge \  
python \  
py-pip \  
&& pip install --upgrade pip \  
&& pip install requests \  
# Clean up  
&& rm -rf \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
  
# Expose ports  
EXPOSE 9091/tcp  
EXPOSE 51413/tcp  

