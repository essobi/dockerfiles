# Docker file for ros-weave  
FROM alpine  
MAINTAINER Ishi Ruy <dev@nhz.io>  
  
RUN apk add -U docker  
RUN curl -L git.io/weave > /sbin/weave && chmod a+x /sbin/weave  
  
ENV SYSTEM_DOCKER /var/run/system-docker.sock  
ENV SWARM_DOCKER /var/run/swarm-docker.sock  
ENV WEAVE_DOCKER /var/run/weave-docker.sock  
ENV DOCKER_HOST unix://$SYSTEM_DOCKER  
  
ENV WEAVEROUTER_NICKNAME foobar  
ENV WEAVEROUTER_PASSWORD barfoo  
  
ENV WEAVEPROXY_HOST 0.0.0.0  
ENV WEAVEPROXY_PORT 12375  
ENV WEAVEROUTER_HEAD_NODE localhost  
ENV WEAVEROUTER_PEER_COUNT 3  
ENV WEAVE_DOCKER_ARGS "--restart=always \  
-v $SWARM_DOCKER:/var/run/docker.sock \  
\--env=DOCKER_HOST=unix:///var/run/docker.sock"  
ENV WEAVEPROXY_DOCKER_ARGS "--restart=always \  
-v $SWARM_DOCKER:/var/run/docker.sock \  
-v /etc/docker/tls:/tls:ro --tlsverify \  
\--tlscacert=/tls/ca.pem \  
\--tlscert=/tls/server-cert.pem \  
\--tlskey=/tls/server-key.pem \  
-H=tcp://$WEAVEPROXY_HOST:$WEAVEPROXY_PORT \  
-H=unix://$WEAVE_DOCKER \  
\--env=DOCKER_HOST=unix:///var/run/docker.sock"  
ENV WEAVEROUTER_ARGS "--password $WEAVEROUTER_PASSWORD \  
\--nickname $WEAVEROUTER_NICKNAME \  
\--init-peer-count $INIT_PEER_COUNT"  
CMD while [ ! -S /var/run/swarm-docker.sock ]; do sleep 1; done; \  
docker ps | grep -i weave-router > /dev/null; \  
if [ $? -ne 0 ]; then \  
weave launch-router $WEAVEROUTER_ARGS; \  
fi; \  
docker ps | grep -i weave-proxy > /dev/null; \  
if [ $? -ne 0 ]; then \  
weave launch-proxy $WEAVEPROXY_ARGS; \  
fi; \  
docker ps | grep -i weave-plugin > /dev/null; \  
if [ $? -ne 0 ]; then \  
weave launch-plugin; \  
fi; \  
weave connect $WEAVEROUTER_HEAD_NODE;  

