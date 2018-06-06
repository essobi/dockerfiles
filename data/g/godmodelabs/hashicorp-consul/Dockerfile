FROM alpine:latest  
MAINTAINER it-operations@boerse-go.de  
ENV TOOL=consul \  
VERSION=1.0.2 \  
SHA256=418329f0f4fc3f18ef08674537b576e57df3f3026f258794b4b4b611beae6c9b  
  
# By using ADD there is no need to install wget or curl  
ADD
https://releases.hashicorp.com/${TOOL}/${VERSION}/${TOOL}_${VERSION}_linux_amd64.zip
${TOOL}_${VERSION}_linux_amd64.zip  
RUN echo "${SHA256} ${TOOL}_${VERSION}_linux_amd64.zip" | sha256sum -cw &&\  
unzip ${TOOL}_${VERSION}_linux_amd64.zip &&\  
rm -r ${TOOL}_${VERSION}_linux_amd64.zip  
  
# additional software for health checks of services  
RUN apk --no-cache add curl monitoring-plugins  
  
ENTRYPOINT ["/consul"]  

