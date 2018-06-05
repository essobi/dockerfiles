FROM docker as docker  
FROM alpine  
  
MAINTAINER Yosuke Matsusaka <yosuke.matsusaka@gmail.com>  
  
RUN apk add --no-cache tini iptables  
  
COPY \--from=docker /usr/local/bin/docker /bin/docker  
  
RUN apk add --no-cache --virtual .staticpython_builddep curl && \  
curl -L
https://github.com/pts/staticpython/raw/master/release/python2.7-static -o
/bin/python && \  
chmod a+x /bin/python && \  
apk del .staticpython_builddep  
  
ADD docker-host-network-firewall.py .  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["/bin/python", "docker-host-network-firewall.py"]

