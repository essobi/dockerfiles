FROM frolvlad/alpine-glibc:alpine-3.7  
MAINTAINER sohrab <sohrab.hosseini@gmail.com>  
RUN \  
apk add \--update ca-certificates && \  
wget -q -O /tmp/openshift-client.tar.gz \  
https://github.com/openshift/origin/releases/download/v3.7.2/openshift-origin-
client-tools-v3.7.2-282e43f-linux-64bit.tar.gz && \  
tar -xvf /tmp/openshift-client.tar.gz \--strip-components 1 -C /tmp && \  
mv -v /tmp/oc /bin && \  
rm -rfv /tmp/* /var/cache/apk/*  
CMD [ "oc" ]

