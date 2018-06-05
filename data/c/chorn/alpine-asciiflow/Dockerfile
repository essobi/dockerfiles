FROM alpine:3.3  
MAINTAINER Chris Horn <chorn@chorn.com>  
  
WORKDIR /usr/src  
  
RUN apk add --update --no-cache --quiet python curl openjdk8-jre \  
&& curl -sSL https://github.com/lewish/asciiflow2/archive/master.tar.gz | tar
xz \  
&& mv asciiflow2-master/* . \  
&& ./compile.sh \  
&& apk del --quiet openjdk8-jre curl \  
&& rm -fr asciiflow2-master.tar.gz asciiflow2-master closure-compiler.jar
compile.sh /var/cache  
  
EXPOSE 8080  
ENTRYPOINT ["python", "-m","SimpleHTTPServer", "8080"]  
  

