FROM alpine  
MAINTAINER Jesus Lopez <jesus@sgn.com>  
  
RUN set -x && \  
apk --no-cache -q add \  
tini  
  
COPY profile.d /etc/profile.d/  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/bin/ash", "-l"]  

