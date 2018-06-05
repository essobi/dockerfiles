FROM alpine:3.7  
  
RUN apk --no-cache add \--update ca-certificates openssl curl tzdata \  
&& curl -sLo /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& curl -sLO https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.26-r0/glibc-2.26-r0.apk \  
&& curl -sLO https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.26-r0/glibc-bin-2.26-r0.apk \  
&& apk add glibc-2.26-r0.apk \  
&& apk add glibc-bin-2.26-r0.apk \  
&& rm glibc-2.26-r0.apk glibc-bin-2.26-r0.apk /etc/apk/keys/sgerrand.rsa.pub \  
&& cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime \  
&& echo "Europe/Amsterdam" > /etc/timezone  
  
COPY bin/remote-file-* /bin/  
RUN chmod +x /bin/remote-file-*  
  
RUN remote-file-download
https://github.com/r-kok/dockerfy/releases/download/2.0.0/dockerfy
1463f73e431e770c650c7c4109fab6bd2a5232f59a4ac7feada055b83b939d17 /bin/dockerfy
\  
&& chmod +x /bin/dockerfy  
  
# This folder is used by dockerfy  
RUN mkdir -p /.secrets \  
&& chmod -R 777 /.secrets  

