from frolvlad/alpine-glibc  
  
ENV BUILD_DEPS="git apache-ant groff less tar gzip python py2-pip" \  
RUN_DEPS="bash supervisor openssh-client openjdk8-jre nodejs curl"  
RUN apk update  
RUN apk add --update $RUN_DEPS $BUILD_DEPS  
  
RUN curl --silent
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein && \  
chmod +x /usr/local/bin/lein  
  
RUN \  
pip install --upgrade pip && \  
pip install --upgrade awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  

