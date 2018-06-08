# We need a go compiler.  
FROM segment/golang:latest  
  
# Copy the ecs-host-manager sources so they can be built within the container.  
COPY . /go/src/github.com/segmentio/ecs-host-manager  
  
# Build ecs-host-manager, then cleanup all unneeded packages.  
RUN cd /go/src/github.com/segmentio/ecs-host-manager && \  
govendor sync && \  
go build -o /usr/local/bin/ecs-host-manager && \  
apt-get remove -y apt-transport-https build-essential git curl docker-engine
&& \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /go/* /usr/local/go /usr/src/Makefile*  
  
# Sets the container's entry point.  
ENTRYPOINT ["ecs-host-manager"]  

