  
FROM alpine:3.7  
  
ENV \  
TERM=xterm \  
BUILD_DATE="2018-01-19"  
  
LABEL \  
version="1801" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile"  
#
---------------------------------------------------------------------------------------  
RUN \  
apk update --quiet --no-cache && \  
apk upgrade \--quiet --no-cache && \  
apk add \--quiet --no-cache \  
bash \  
openssl  
  
COPY generate-certs /usr/bin/generate-certs  
  
VOLUME [ "/certs" ]  
WORKDIR "/certs"  
  
CMD [ "/usr/bin/generate-certs" ]  

