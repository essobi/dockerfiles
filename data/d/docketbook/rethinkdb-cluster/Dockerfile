FROM docketbook/rethinkdb-consul:2.3.5  
MAINTAINER Tom Midson <tm@docketbook.io>  
  
USER root  
  
RUN set -x \  
&& curl -Lso /tmp/rethinkdb-health.tar.gz \  
"https://github.com/docketbook/rethinkdb-containerpilot-
health/releases/download/0.2/rethinkdb-health-0.2-linux.tar.gz" \  
&& tar zxf /tmp/rethinkdb-health.tar.gz -C /usr/local/bin \  
&& rm /tmp/rethinkdb-health.tar.gz  
  
ENV CONTAINERPILOT file:///etc/containerpilot.json  
  
# configure ContainerPilot and RethinkDB  
COPY etc/* /etc/  
  
EXPOSE 29015 28015 8080  
ENTRYPOINT []  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
# use --console to get error logs to stderr  
CMD [ "containerpilot", \  
"rethinkdb", \  
"--config-file", \  
"/etc/rethink.conf", \  
"--bind", \  
"all" \  
]  

