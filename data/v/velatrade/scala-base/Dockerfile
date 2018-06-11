FROM java:openjdk-8  
# ################################  
# SBT and Scala setup  
# ################################  
ENV SBT_OPTS -Xmx384m -Xss512k -XX:+UseCompressedOops
-Dsbt.jse.engineType=Node  
  
# Install and update SBT  
RUN apt-get update  
RUN apt-get install -y apt-transport-https  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN apt-get update && apt-get install -y sbt  
RUN sbt update  
  
# Global Scala/SBT settings  
WORKDIR /root/.sbt/0.13  
COPY global/plugins plugins  
RUN sbt update  
COPY global/build.sbt build.sbt  
  
# Let's get initial sbt deps and compile 'compiler-interface'  
WORKDIR /var/velatrade  
COPY build.sbt build.sbt  
COPY project project  
RUN sbt update  
  
COPY Hello.scala Hello.scala  
RUN sbt compile  
  
# Cleanup  
RUN rm -r build.sbt Hello.scala project target  

