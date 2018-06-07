FROM golang:1.4  
  
ENV PATH=${PATH}:/usr/local/bin  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs  
  
RUN apt-get update && \  
apt-get install -y python3-pip bash curl telnet unzip && \  
apt-get install -y dnsutils dstat vim ca-certificates procps && \  
pip3 install awscli && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/cache/apt/archives/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -fsSLO
https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz && tar xzvf
docker-17.04.0-ce.tgz && mv docker/docker /usr/local/bin && rm -r docker
docker-17.04.0-ce.tgz  
  
RUN curl -OL
https://github.com/google/protobuf/releases/download/v3.4.0/protoc-3.4.0-linux-x86_64.zip
&& \  
unzip protoc-3.4.0-linux-x86_64.zip -d protoc-3.4.0 && \  
mv protoc-3.4.0/bin/protoc /usr/local/bin && \  
go get github.com/golang/protobuf/protoc-gen-go && \  
go build github.com/golang/protobuf/protoc-gen-go && \  
mv protoc-gen-go /usr/local/bin

