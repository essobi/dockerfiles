FROM scispike/node:0.31.1  
# NOTE: The image created by this Dockerfile only adds packages that are  
# required for yaktor to run properly. It does NOT install yaktor; see  
# the file Dockerfile or Dockerfile.dev for that.  
MAINTAINER yaktor@scispike.com  
  
RUN \  
set -x \  
&& \  
apk add --no-cache \  
openjdk7-jre-base \  
ruby-dev=2.3.1-r0 \  
ruby=2.3.1-r0 \  
ghostscript-fonts \  
graphviz  
  
RUN \  
/usr/bin/gem install -N \  
asciidoctor-diagram \  
json  
  
VOLUME ["/app"]  
WORKDIR /app  
  
COPY yaktor.sh /yaktor.sh  
ENTRYPOINT ["/yaktor.sh"]  

