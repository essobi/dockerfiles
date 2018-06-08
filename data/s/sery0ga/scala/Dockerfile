# Scala, sbt, Boxfuse and FlyWayon Java 8  
#  
# URL: https://github.com/HappyMelly/docker-scala  
#  
# forked from: bad79s/scala  
# - https://github.com/William-Yeh/docker-scala  
#  
# Version 0.3  
FROM sery0ga/scala  
MAINTAINER sery0ga <skotlov@gmail.com>  
  
ENV ACTIVATOR_VERSION 1.3.8  
ENV SBT_VERSION 0.13.12  
ENV BOXFUSE_VERSION 1.22.2.1149  
ENV FLYWAYDB_VERSION 4.0.3  
ENV BOXFUSE_DIR boxfuse-commandline-$BOXFUSE_VERSION  
ENV SCALA_TARBALL http://www.scala-lang.org/files/archive/scala-2.11.8.deb  
ENV SBT_TARBALL https://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz  
ENV ACTIVATOR https://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION-minimal.zip  
ENV BOXFUSE https://files.boxfuse.com/com/boxfuse/client/boxfuse-
commandline/$BOXFUSE_VERSION/$BOXFUSE_DIR.tar.gz  
ENV FLYWAYDB https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/$FLYWAYDB_VERSION/flyway-commandline-$FLYWAYDB_VERSION.tar.gz  
  
RUN echo "===> Update APT " && \  
apt-get update && apt-get install -y \  
unzip git  
  
# RUN echo "===> install from Typesafe repo (contains old versions but they
have all dependencies we need later on)" && \  
# DEBIAN_FRONTEND=noninteractive \  
# apt-get install -y --force-yes wget && \  
# wget http://apt.typesafe.com/repo-deb-build-0002.deb && \  
# dpkg -i repo-deb-build-0002.deb && \  
# apt-get update  
RUN echo "===> install Scala" && \  
# DEBIAN_FRONTEND=noninteractive \  
# apt-get install -y --force-yes libjansi-java && \  
wget -nv $SCALA_TARBALL && \  
dpkg -i scala-*.deb  
  
RUN echo "===> install sbt" && \  
cd /tmp && \  
wget $SBT_TARBALL && \  
tar xzf *.tgz && \  
cp -f sbt/bin/* /usr/local/bin/  
  
RUN echo "===> get activator" && \  
cd /usr/local/bin && \  
rm -rf activator* && \  
wget $ACTIVATOR && \  
unzip *.zip && \  
rm *.zip && \  
cd /  
  
ENV PATH /usr/local/bin/activator-$ACTIVATOR_VERSION-minimal/bin/:$PATH  
  
RUN echo "====> install activator" && \  
cd /tmp && \  
activator new dummy play-scala && \  
rm -rf dummy  
  
RUN echo "====> install boxfuse" && \  
cd /usr/local/bin/ && \  
rm -rf boxfuse* && \  
wget $BOXFUSE && \  
tar xzf $BOXFUSE_DIR.tar.gz && \  
rm $BOXFUSE_DIR.tar.gz  
  
ENV PATH /usr/local/bin/boxfuse:$PATH  
  
RUN echo "====> install flywaydb" && \  
cd /usr/local/bin && \  
wget https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/4.0.3/flyway-commandline-4.0.3.tar.gz && \  
tar xzf *.tar.gz && \  
rm *.tar.gz  
  
ENV PATH /usr/local/bin/flyway-$FLYWAYDB_VERSION:$PATH  
  
RUN echo "===> install Scala" && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --force-yes curl  
  
RUN echo "===> clean up..." && \  
rm -f *.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# create an empty sbt project;  
# then fetch all sbt jars from Maven repo so that your sbt will be ready to be
used when you launch the image  
COPY test-sbt.sh /tmp/  
RUN cd /tmp && \  
./test-sbt.sh && \  
rm -rf *  
  
# Define default command.  
CMD ["scala"]  

