FROM frolvlad/alpine-glibc:alpine-3.6  
  
RUN apk update && \  
apk add ca-certificates curl openssl git && \  
update-ca-certificates  
  
ENV
DOWNLOAD_URL=https://github.com/openshift/origin/releases/download/v3.6.0/openshift-
origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz  
  
RUN wget $DOWNLOAD_URL -O oc.tar.gz && \  
tar xf oc.tar.gz && \  
mv */oc /usr/local/bin/ && \  
rm oc.tar.gz  

