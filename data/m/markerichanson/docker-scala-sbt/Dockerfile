FROM markerichanson/docker-scala:2.11.8  
ARG SBT_VERSION  
  
RUN \  
curl -fsL https://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz | tar xfz - -C /usr/share/  
  
ENV PATH /usr/share/sbt-launcher-packaging-$SBT_VERSION/bin:$PATH  
  
WORKDIR /tmp  
  
RUN echo 'object Hi { def main(args: Array[String]) = println("Hi!") }' >
hw.scala  
RUN sbt  
RUN rm -rf hw.scala  
  
VOLUME ["/root/project"]  
VOLUME ["/root/.ivy2"]  
  
WORKDIR /root/project  
  
#ENTRYPOINT ["sbt"]  

