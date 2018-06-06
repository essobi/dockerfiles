# Scala for Ubuntu 14.04  
#  
# GitHub - http://github.com/dalekurt/docker-scala  
# Docker Hub - http://hub.docker.com/u/dalekurt/scala  
# Twitter - http://www.twitter.com/dalekurt  
FROM dalekurt/java7  
  
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"  
ENV SCALA_VERSION 2.11.6  
ENV SBT_VERSION 0.13.8  
ENV SCALA_TARBALL http://www.scala-
lang.org/files/archive/scala-${SCALA_VERSION}.deb  
ENV SBT_JAR https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/${SBT_VERSION}/sbt-launch.jar  
  
RUN apt-get update; apt-get install -y maven  
  
# Typesafe repo (contains old versions but they have all dependencies we need
later on)  
RUN wget http://apt.typesafe.com/repo-deb-build-0002.deb  
RUN dpkg -i repo-deb-build-0002.deb  
RUN rm -f repo-deb-build-0002.deb  
  
RUN wget -nv $SCALA_TARBALL  
RUN dpkg -i scala-${SCALA_VERSION}.deb  
  
RUN wget -nv -P /usr/local/bin/ $SBT_JAR  
  
# clean up  
RUN rm -f *.deb  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# make sbt executable  
ADD scripts/sbt /usr/local/bin/  
RUN chmod +x /usr/local/bin/sbt  
  
# Create an empty sbt project  
#ADD scripts/test-sbt.sh /tmp/  
#RUN cd /tmp && \  
# ./test-sbt.sh && \  
# rm -rf *  
EXPOSE 9000  
#RUN mkdir /opt/app  
#WORKDIR /opt/app  
# Define default command.  
#ENTRYPOINT ["mvn"]  
#CMD ["install"]  
#WORKDIR /opt/app/mystuff-play-scala-webapp  
#ENTRYPOINT ["sbt"]  
#CMD ["run"]  

