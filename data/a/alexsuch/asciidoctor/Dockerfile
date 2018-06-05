FROM alpine:latest  
  
MAINTAINER Alejandro Such <alejandro.such@gmail.com>  
  
RUN apk update \  
&& apk add \--no-cache ca-certificates ruby ruby-rdoc ruby-irb ruby-dev build-
base zlib-dev curl \  
&& update-ca-certificates \  
&& gem update \  
&& gem install asciidoctor coderay \  
&& gem install --pre asciidoctor-pdf asciidoctor-epub3 \  
&& wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz
-O - | tar -xzf - -C /usr/bin kindlegen \  
&& apk del ca-certificates ruby-dev build-base zlib-dev curl \  
&& rm -rf /tmp/* /var/cache/apk/* *.tar.gz  
  
ENV KINDLEGEN /usr/bin/kindlegen  

