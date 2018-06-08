FROM tcaxias/orchestrator  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
ENV \  
DEPS="ca-certificates git go build-base" \  
PKGS="py-setuptools python"  
RUN \  
apk add --update --no-cache $DEPS $PKGS \  
&& go get github.com/prometheus/graphite_exporter \  
&& mv $GOPATH/bin/* /usr/local/bin/ \  
&& easy_install-2.7 pip \  
&& pip install -U pip \  
&& pip install supervisor \  
&& apk del $DEPS \  
&& rm -rf /tmp/*  
  
RUN adduser -D app  
  
ADD \  
supervisord.conf \  
orchestrator.conf.json \  
/etc/  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-j",
"/dev/shm/supervisor.pid", "-l", "/dev/null" ]  
  
EXPOSE 3000 9108  
ENV TERM=xterm  

