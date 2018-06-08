FROM peelsky/zulu-openjdk-busybox  
MAINTAINER Piotr Limanowski <plimanowski@gmail.com>  
  
ENV SBT_VERSION 0.13.7  
RUN (curl -o /tmp/sbt.zip -L http://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.zip &&\  
unzip /tmp/sbt.zip -d /opt &&\  
echo 'java $SBT_OPTS -jar `dirname $0`/sbt-launch.jar "$@"' > /bin/sbt &&\  
chmod a+x /bin/sbt &&\  
#ln -s /opt/sbt/bin/sbt /bin/sbt &&\  
#ln -s /opt/sbt/bin/sbt-launch-lib.bash /bin/sbt-launch-lib.bash &&\  
ln -s /opt/sbt/bin/sbt-launch.jar /bin/sbt-launch.jar &&\  
ln -s /opt/sbt/conf/sbtopts /etc/sbtopts &&\  
rm /tmp/sbt.zip)  
  
RUN sbt exit  
  
ONBUILD ADD . /app  
ONBUILD WORKDIR /app  
ONBUILD RUN sbt update  
  
CMD sbt  

