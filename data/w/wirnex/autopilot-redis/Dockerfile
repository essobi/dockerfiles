FROM redis:alpine  
MAINTAINER Igor Pletenev <igor@wirnex.com>  
  
RUN apk update && \  
apk add curl && \  
rm -rf /var/cache/apk/*  
  
# Install ContainerPilot  
ENV CONTAINERPILOT_VERSION 2.6.0  
RUN export CP_SHA1=c1bcd137fadd26ca2998eec192d04c08f62beb1f \  
&& curl -Lso /tmp/containerpilot.tar.gz \  
"https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz"
\  
&& echo "${CP_SHA1} /tmp/containerpilot.tar.gz" | sha1sum -c \  
&& tar zxf /tmp/containerpilot.tar.gz -C /bin \  
&& rm /tmp/containerpilot.tar.gz  
  
# COPY ContainerPilot configuration  
ENV CONTAINERPILOT_PATH=/etc/containerpilot.json  
COPY containerpilot.json ${CONTAINERPILOT_PATH}  
ENV CONTAINERPILOT=file://${CONTAINERPILOT_PATH}  
  
ENTRYPOINT ["/bin/containerpilot"]  
  
EXPOSE 6379  
CMD ["containerpilot", "/usr/local/bin/docker-entrypoint.sh", "redis-server"]  

