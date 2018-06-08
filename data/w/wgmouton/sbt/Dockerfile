FROM wgmouton/java:latest  
  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
COPY Properties /  
# Install sbt  
RUN . /Properties &&\  
apk add --update curl ca-certificates bash && \  
curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built &&\  
apk del curl | rm /Properties  
  
# Define working directory  
WORKDIR /app

