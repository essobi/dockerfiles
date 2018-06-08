#FROM alpine:3.5  
FROM java:8-jdk  
  
MAINTAINER xsota  
  
VOLUME ["/minecraft/app"]  
  
WORKDIR /minecraft  
  
ARG VERSION="--rev 1.12.2"  
ENV XMS="1024m" \  
XMX="1024m" \  
EULA="false"  
ADD
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
tmp/BuildTools.jar  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
#RUN apt-get update \  
# && apt-get install \  
# && openjdk-8-jdk-headless openjdk-8-jre openjdk-8-jdk  
#RUN echo "http://dl-3.alpinelinux.org/alpine/v3.5/community/" >>
/etc/apk/repositories \  
# && apk update \  
# && apk add --no-cache \  
# bash gcc make perl libc-dev\  
# ca-certificates \  
# openjdk8 \  
# openssl \  
# git \  
# bash \  
# && wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
# && wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk \  
# && apk add glibc-2.25-r0.apk \  
# && java -jar tmp/BuildTools.jar $VERSION \  
# && rm -rf tmp/*  
RUN cd tmp \  
&& java -jar BuildTools.jar $VERSION \  
&& cp spigot-*.jar /minecraft/spigot.jar \  
&& rm -rf /minecraft/tmp/*  
  
WORKDIR /minecraft/app  
  
CMD /usr/local/bin/run.sh  
  
EXPOSE 25565  

