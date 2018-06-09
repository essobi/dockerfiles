#  
# Dockerfile  
#  
FROM debian:stretch-slim  
MAINTAINER Matej Kovac <matej.kovac@gmail.com>  
  
# assets - big, pre-downloaded files, not modified very often  
#  
#COPY assets /root/assets  
# files and scripts needed to build the image  
#  
COPY build /root/build  
  
ARG CACHE_DATE=1970-01-01  
RUN run-parts --report --exit-on-error /root/build/scripts && \  
rm -rfv /root/build /root/assets  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  
CMD ["/usr/bin/dumb-init", "/etc/rc.local"]  

