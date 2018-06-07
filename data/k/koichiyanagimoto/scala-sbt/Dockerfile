FROM centos:latest  
  
ENV SCALA_VERSION 2.11.7  
ENV SBT_VERSION 0.13.8  
RUN yum install -y java-1.8.0-openjdk-headless java-1.8.0-openjdk-devel zip
unzip  
  
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0  
RUN \  
cd /usr/local && \  
curl -o scala-$SCALA_VERSION.tgz
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz &&
\  
tar -xf scala-$SCALA_VERSION.tgz && \  
rm scala-$SCALA_VERSION.tgz && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
RUN \  
curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
# Define working directory  
WORKDIR /root  
  
EXPOSE 9000:9000

