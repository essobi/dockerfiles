# NAME: Captain Services Base  
#  
# DESCRIPTION: Captain Services Base for all Captain Services.  
#  
# REQUIRED ENVS:  
#  
# OPTIONAL ENVS:  
#  
# OTHER:  
  
FROM thedutchselection/alpine:3.4  
MAINTAINER Gerard Meijer <g.meijer@thedutchselection.com>  
  
RUN \  
apk update && \  
apk add bash && \  
apk add redis && \  
rm /etc/conf.d/redis && \  
rm /etc/logrotate.d/redis && \  
rm /etc/init.d/redis && \  
rm /etc/redis.conf && \  
rm /usr/share/licenses/redis/COPYING && \  
rm /usr/bin/redis-sentinel && \  
rm /usr/bin/redis-server && \  
rm /usr/bin/redis-benchmark && \  
rm /usr/bin/redis-check-aof && \  
rm /var/cache/apk/*  
  
ADD files/scripts /usr/local/bin  
  
ENTRYPOINT ["/bin/bash"]

