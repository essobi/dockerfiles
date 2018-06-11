# based on https://github.com/synctree/docker-coturn/blob/master/Dockerfile  
FROM debian:sid  
  
MAINTAINER Yuri Vysotskiy (yfix) <yfix.dev@gmail.com>  
  
# XXX: Workaround for https://github.com/docker/docker/issues/6345  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -y \  
coturn \  
curl \  
procps \  
\  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker /  
ADD turnserver.sh /turnserver.sh  
  
EXPOSE 3478 3478/udp  
  
CMD ["/bin/sh", "/turnserver.sh"]  

