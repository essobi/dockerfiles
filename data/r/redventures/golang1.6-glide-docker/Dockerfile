FROM golang:1.6.2  
WORKDIR /root  
  
# install docker  
RUN wget https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz && tar
-xvzf docker-latest.tgz && mv docker/* /usr/bin/ && rm -rf docker*  
# install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-
compose-`uname -s`-`uname -m` > /usr/bin/docker-compose && chmod +x
/usr/bin/docker-compose  
  
# install glide and golang  
ENV GLIDE_VERSION 0.10.2  
ENV GO_PATH /go  
RUN set -xe && \  
curl -Ls
https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-linux-
amd64.tar.gz | tar -xz --strip-components=1 -C /tmp && \  
mv /tmp/glide /usr/local/bin/ && \  
rm -rf /tmp/* && \  
go get github.com/codegangsta/gin  

