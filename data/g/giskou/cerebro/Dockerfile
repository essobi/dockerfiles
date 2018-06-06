ARG GOSU_VERSION=1.10  
ARG CEREBRO_VERSION=0.7.3  
FROM alpine as download-gosu  
  
ARG GOSU_VERSION  
  
WORKDIR /tmp  
  
RUN apk add --update curl gnupg  
RUN curl -Lo gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64"  
RUN curl -Lo gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64.asc"  
  
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN gpg --batch --verify /tmp/gosu.asc /tmp/gosu  
RUN chmod +x gosu  
  
FROM alpine as download-cerebro  
  
ARG CEREBRO_VERSION  
  
WORKDIR /tmp  
  
RUN apk add --update curl gnupg  
RUN curl -Lo /tmp/cerebro.tgz
https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz  
RUN tar zxvf cerebro.tgz  
RUN mv cerebro-${CEREBRO_VERSION} cerebro  
  
FROM openjdk:jre-alpine  
  
RUN apk add --update bash  
  
COPY \--from=download-gosu /tmp/gosu /usr/local/bin/gosu  
RUN gosu nobody true  
  
COPY \--from=download-cerebro /tmp/cerebro /srv/cerebro  
  
EXPOSE 9000  
ENTRYPOINT ["/srv/cerebro/bin/cerebro"]  

