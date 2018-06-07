FROM evild/alpine-base:1.0.0  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
ENV SYNCTHING_VERSION 0.12.21  
ENV SYNCTHING_GUI_PORT 8080  
ENV GOPATH /go  
  
RUN \  
build_pkgs="curl go" \  
&& apk --no-cache add ${build_pkgs} \  
&& mkdir -p ${GOPATH}/src/github.com/syncthing && cd
${GOPATH}/src/github.com/syncthing \  
&& curl -SLO
https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/syncthing-
source-v$SYNCTHING_VERSION.tar.gz \  
&& curl -SLO
https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/sha256sum.txt.asc
\  
&& sha256sum -c sha256sum.txt.asc 2>&1 |grep -q OK \  
&& tar zxf syncthing-source-v$SYNCTHING_VERSION.tar.gz \  
&& cd syncthing \  
&& go run build.go \  
&& cp $GOPATH/src/github.com/syncthing/syncthing/bin/* /usr/local/bin \  
&& apk del ${build_pkgs} \  
&& rm -rf ${GOPATH} /tmp/* /var/cache/apk/* /root/.n* \  
  
EXPOSE 22000 21025/udp  
  
ADD root /  

