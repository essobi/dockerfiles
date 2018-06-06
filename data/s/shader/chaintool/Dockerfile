FROM znly/protoc  
MAINTAINER Samuel Christie <emailium@gmail.com>  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u111  
ENV JAVA_ALPINE_VERSION 8.111.14-r0  
  
RUN set -x \  
&& apk add --no-cache \  
git bash wget ca-certificates go pkgconf \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "${JAVA_HOME}/bin/javac" = "$(which javac)" ] \  
&& git clone https://github.com/hyperledger/fabric-chaintool \  
&& cd fabric-chaintool \  
&& git checkout v0.9.1 \  
&& make install  
  
RUN echo -e "#!/bin/sh\nexec chaintool \$@" >/chaintool.sh \  
&& cat /chaintool.sh \  
&& chmod +x /chaintool.sh  
  
ENTRYPOINT ["/chaintool.sh"]  
VOLUME /src  
VOLUME /dest  
WORKDIR /src  

