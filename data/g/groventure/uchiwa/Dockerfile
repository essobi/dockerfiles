FROM golang:1.5  
MAINTAINER Hellyna NG <hellyna@groventure.com>  
  
COPY scripts/prebuild.sh /docker-scripts/  
RUN /bin/bash /docker-scripts/prebuild.sh  
  
USER uchiwa  
ENV GOPATH="$HOME/go"  
ENV PATH="$PATH:$GOPATH/bin"  
COPY scripts/build.sh /docker-scripts/  
RUN /bin/bash /docker-scripts/build.sh  
  
ENV UCHIWA_PATH="$GOPATH/src/github.com/sensu/uchiwa"  
WORKDIR "$UCHIWA_PATH"  
COPY templates/* /docker-templates/  
COPY scripts/entrypoint.sh /docker-scripts/  
  
VOLUME ["/docker-templates"]  
  
ENTRYPOINT ["/bin/bash", "/docker-scripts/entrypoint.sh"]  

