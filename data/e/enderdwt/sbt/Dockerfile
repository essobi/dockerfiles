FROM enderdwt/java  
  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
  
#Install sbt  
ENV SBT_VERSION 0.13.13  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN wget https://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.zip \  
&& unzip sbt-${SBT_VERSION}.zip -d /usr/local/ \  
&& rm sbt-${SBT_VERSION}.zip  
  
RUN mkdir /app  
  
WORKDIR /app  

