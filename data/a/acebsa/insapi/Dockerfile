# VERSION v0.1.0  
# DOCKER-VERSION v1.6.0  
# INSAPI-VERSION v2.0.0  
# AUTHOR: Joan Llopis <jllopis@acb.es>  
# DESCRIPTION: Imagen con la API de Inscripciones ACB  
# TO_BUILD: docker build --rm -t docker.acb.info:5000/insapi:{version} .  
# TO_RUN: docker run -t -d -link dbins:db.acb.info -p 8000
docker.acb.info:5000/insapi:{version}  
FROM golang:1.4.2-wheezy  
MAINTAINER Joan Llopis <jllopis@acb.es>  
  
ENV INSAPI_VERSION v2.0.0  
ENV APP bitbucket.org/acbins/desarrollo/backend  
  
ADD . /go/src/${APP}  
  
WORKDIR /go/src/${APP}  
RUN go get github.com/tools/godep \  
&& godep go install ${APP} \  
&& mkdir -p /etc/insapi/certs  
  
EXPOSE 8000  
VOLUME ["/etc/insapi/certs"]  
  
ENTRYPOINT /go/bin/backend  

