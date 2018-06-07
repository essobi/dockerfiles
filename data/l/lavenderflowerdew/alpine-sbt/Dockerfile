FROM lavenderflowerdew/alpine-base:latest  
  
ARG INSTALL_SBT_VERSION=0.13.15  
ARG SBT_VERSION=0.13.15  
ARG JDK_VERSION=8  
LABEL maintainer "lavender.flowerdew@gmail.com" java.version=$JDK_VERSION  
  
# Development Tools Install  
RUN apk update && apk upgrade && \  
apk --no-cache add \  
git \  
openjdk$JDK_VERSION \  
vim  
  
# Install SBT  
RUN cd /usr/share && \  
wget -O sbt.zip "https://bintray.com/sbt/native-
packages/download_file?file_path=sbt%2F${INSTALL_SBT_VERSION}%2Fsbt-${INSTALL_SBT_VERSION}.zip"
&& \  
unzip sbt.zip && \  
rm sbt.zip && \  
ln -s /usr/share/sbt/conf /etc/sbt && \  
ln -s /usr/share/sbt/bin/sbt /usr/bin && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
# Clean Up  
RUN rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
# Set Up Development Environment  
USER flower  
ENV /home/flower  
WORKDIR /home/flower  
RUN cd /home/flower/ && \  
mkdir -p /home/flower/dev && \  
mkdir -p /home/flower/tmp1/project && \  
cd /home/flower/tmp1 && \  
echo 'object Hi { def main(args: Array[String]) = println("Hi!") }' >>
hw.scala && \  
echo "sbt.version=${SBT_VERSION}" >> ./project/build.properties && \  
/usr/share/sbt/bin/sbt compile && \  
cd .. && \  
rm -rf /home/flower/target /home/flower/project /home/flower/tmp*  
  
ENTRYPOINT ["/bin/bash", "-c"]  
  
CMD ["sbt -v"]  

