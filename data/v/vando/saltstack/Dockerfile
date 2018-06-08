FROM alpine:3.3  
MAINTAINER Facundo Bianco <vando@van.do>  
  
ENV TERM xterm  
  
RUN apk add --no-cache python py-crypto py-jinja2 py-tornado py-yaml  
RUN apk add --no-cache -X http://dl-4.alpinelinux.org/alpine/edge/testing py-
msgpack py-zmq salt  
  
RUN mkdir -p /srv/salt /srv/pillar  
RUN chmod 0700 /srv/pillar  
  
RUN sed -i 's/^#master: salt/master: 127.0.0.1/;s/^#id:/id: minion/'
/etc/salt/minion  
RUN sed -i 's/^#worker_threads: 5/worker_threads: 20/' /etc/salt/master  
RUN apk add --no-cache -X http://dl-4.alpinelinux.org/alpine/edge/testing  
RUN salt-master -d && salt-minion -d && while(true) ; do salt-key -yA && break
|| sleep 15 ; done  
  
ADD saltstack.run /usr/local/bin/saltstack.run  
RUN chmod +x /usr/local/bin/saltstack.run  
  
EXPOSE 4505 4506  
VOLUME ["/srv/salt", "/srv/pillar"]  
CMD ["/usr/local/bin/saltstack.run"]  

