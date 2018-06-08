FROM rodrigosaito/java:8  
ENV MAVEN_BASE_PATH /usr/lib/maven  
ENV MAVEN_VERSION 3.3.3  
ENV MAVEN_HOME $MAVEN_BASE_PATH/maven  
ENV PATH ${PATH}:${MAVEN_HOME}/bin  
  
RUN apk --update --virtual=build-dependencies add curl ca-certificates tar \  
&& mkdir $MAVEN_BASE_PATH \  
&& curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C $MAVEN_BASE_PATH \  
&& ln -s $MAVEN_BASE_PATH/apache-maven-$MAVEN_VERSION $MAVEN_BASE_PATH/maven \  
&& apk del build-dependencies  
  
ENTRYPOINT [ "mvn" ]  

