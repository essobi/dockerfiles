FROM alpine:3.3  
LABEL maintainer "kutuni"  
  
# Default to UTF-8 file.encoding  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
# grab su-exec for easy step-down from root  
# and bash for "bin/elasticsearch" among others  
RUN apk add --no-cache curl bash tar  
  
RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu  
  
RUN mkdir /etc/security; \  
echo "* - nofile 65535" > /etc/security/limits.conf; \  
echo "* - memlock unlimited" >> /etc/security/limits.conf; \  
echo vm.max_map_count=262144 >> /etc/sysctl.conf; \  
echo vm.swappiness=0 >> /etc/sysctl.conf; \  
echo net.ipv6.conf.all.disable_ipv6 = 1 >> /etc/sysctl.conf; \  
echo net.ipv6.conf.default.disable_ipv6 = 1 >> /etc/sysctl.conf; \  
echo net.ipv6.conf.lo.disable_ipv6 = 1 >> /etc/sysctl.conf ;  
  
CMD bash  

