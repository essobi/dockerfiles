FROM alpine:3.4  
LABEL maintainer="Kazumichi Yamamoto <yamamoto.febc@gmail.com>"  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
ENV SACLOUD_BALUS_VERSION=0.0.1  
RUN set -x && apk add --no-cache --update zip ca-certificates  
  
ADD https://github.com/yamamoto-febc/sacloud-
balus/releases/download/v${SACLOUD_BALUS_VERSION}/sacloud-balus_linux-
amd64.zip ./  
RUN unzip sacloud-balus_linux-amd64.zip -d /bin; rm -f sacloud-balus_linux-
amd64.zip  
  
ENTRYPOINT ["/bin/sacloud-balus"]  

