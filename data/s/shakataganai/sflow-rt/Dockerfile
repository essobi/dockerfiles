# Generated originally via:  
# docker pull sflow/sflow-rt >/dev/null && docker images | grep sflow/sflow-rt
| head -n1 | \  
# awk '{print $3}' | xargs docker run -v
/var/run/docker.sock:/var/run/docker.sock --rm chenzj/dfimage  
FROM openjdk:8-jre-alpine  
CMD ["/bin/sh"]  
RUN apk add --no-cache curl \  
&& curl -sLOk http://www.inmon.com/products/sFlow-RT/sflow-rt.tar.gz \  
&& tar -xzf sflow-rt.tar.gz \  
&& rm sflow-rt.tar.gz \  
&& addgroup -S sflowrt \  
&& adduser -S -h /sflow-rt -g sFlow-RT -G sflowrt -s /sbin/nologin sflowrt \  
&& chown -R sflowrt:sflowrt sflow-rt  
EXPOSE 6343/udp 8008  
USER sflowrt  
WORKDIR /sflow-rt  
ENV RTMEM=1G LANG=en_US.UTF-8  
HEALTHCHECK CMD curl -sf http://localhost:8008/version || exit 1  
CMD ["/sflow-rt/start.sh"]  

