FROM taig/scala:1.0.8  
MAINTAINER Niklas Klein "mail@taig.io"  
ENV ACTIVATOR 1.3.12  
WORKDIR /root/  
  
RUN apt-get install -y --no-install-recommends unzip  
RUN apt-get clean  
  
RUN wget https://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR/typesafe-activator-$ACTIVATOR-minimal.zip  
RUN unzip ./typesafe-activator-$ACTIVATOR-minimal.zip  
ENV PATH $PATH:/root/activator-$ACTIVATOR-minimal/bin  
RUN rm -r ./typesafe-activator-$ACTIVATOR-minimal.zip  
RUN activator new sample play-scala  
RUN echo "sbt.version=${SBT}" > ./sample/project/build.properties  
RUN echo "scalaVersion := \"${SCALA}\"" >> ./sample/build.sbt  
RUN cd ./sample/ && sbt test  
RUN rm -r ./sample/  

