FROM alpine:3.4  
LABEL maintainer="Kazumichi Yamamoto <yamamoto.febc@gmail.com>"  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
ENV SACKEREL_VERSION=0.0.3  
RUN set -x && apk add --no-cache --update zip ca-certificates  
  
ADD
https://github.com/sacloud/sackerel/releases/download/v${SACKEREL_VERSION}/sackerel_linux-
amd64.zip ./  
RUN unzip sackerel_linux-amd64.zip -d /bin; rm -f sackerel_linux-amd64.zip  
  
ENTRYPOINT ["/bin/sackerel"]  

