FROM hokiegeek/scala:latest  
  
WORKDIR /tmp  
  
RUN wget https://dl.bintray.com/sbt/native-
packages/sbt/0.13.12/sbt-0.13.12.tgz  
  
RUN tar -xvzf sbt-0.13.12.tgz  
RUN cp sbt/bin/* /usr/bin  
  
RUN rm -rf sbt-0.13.12.tgz sbt  
  
RUN echo 'object Hi { def main(args: Array[String]) = println("Hi!") }' >
hw.scala  
RUN sbt  
RUN rm -rf hw.scala  
  
WORKDIR /app  
  
ENTRYPOINT ["sbt"]  

