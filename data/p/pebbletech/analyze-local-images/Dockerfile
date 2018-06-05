FROM golang:1.6  
RUN apt-key adv \  
\--keyserver hkp://pgp.mit.edu:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb http://apt.dockerproject.org/repo debian-jessie main" >> \  
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -y docker-engine && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN go get -u github.com/coreos/clair/contrib/analyze-local-images  
  
ENTRYPOINT ["/go/bin/analyze-local-images"]  
  

