FROM alpine  
MAINTAINER ya.Seregko  
  
RUN set -x \  
&& apk update \  
&& apk add git openjdk8 expect curl sudo  
  
RUN set -x \  
# Create a dev user to use as the directory owner  
&& addgroup dev \  
&& adduser -D -s /bin/sh -G dev dev \  
&& echo "dev:password" | chpasswd \  
  
# Setup wrapper scripts  
&& curl -o /run-as-user https://raw.githubusercontent.com/mkenney/docker-
scripts/master/container/run-as-user \  
&& chmod 0755 /run-as-user  
  
VOLUME /src  
WORKDIR /src  
  
ENTRYPOINT ["/run-as-user"]  
  

