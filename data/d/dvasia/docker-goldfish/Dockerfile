FROM golang:1.10 as build  
  
ENV GOLDFISH_BIN goldfish  
ENV GOLDFISH_VERSION 0.9.0  
ENV GOLDFISH_URL
https://github.com/Caiyeon/goldfish/releases/download/v${GOLDFISH_VERSION}/goldfish-
linux-amd64  
ENV PACKAGES="curl"  
RUN apt-get update \  
&& apt-get -y install ${PACKAGES} \  
&& curl -s -L -o ${GOLDFISH_BIN} "${GOLDFISH_URL}"\  
&& chmod +x ./${GOLDFISH_BIN}  
  
# final stage  
FROM scratch  
ARG PACKAGE  
COPY \--from=build /go/goldfish /goldfish  
COPY \--from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
ENTRYPOINT ["/goldfish -config=/etc/goldfish/config.json"]  

