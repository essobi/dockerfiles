FROM alpine:latest  
  
ENV VERSION=1.0.42  
ENV BUILD_DATE=20170914095800  
ENV CHECKSUM=297b14ed1efe9b894e27e63f7aff36ceded7334c174f5a8602af9e74beb2f512  
  
RUN apk add --update curl openssh tar \  
&& curl -L https://github.com/github/gh-ost/releases/download/v${VERSION}/gh-
ost-binary-linux-${BUILD_DATE}.tar.gz > gh-ost-binary-
linux-${BUILD_DATE}.tar.gz \  
&& echo "${CHECKSUM} gh-ost-binary-linux-${BUILD_DATE}.tar.gz" > gh-ost-
checksum \  
&& sha256sum -cs gh-ost-checksum \  
&& tar zxf gh-ost-binary-linux-${BUILD_DATE}.tar.gz -C /bin \  
&& rm -f gh-ost-binary-linux-${BUILD_DATE}.tar.gz  
  
ENTRYPOINT ["/bin/gh-ost"]  

