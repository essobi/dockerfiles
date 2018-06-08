FROM java:openjdk-8-jdk  
  
ENV BUILD_DIR /build  
ENV APP_DIR /app  
# -Duser.dir=/user is passed to metronone.  
# From there you can set the config like dcos does but use docker run ... -v
`pwd`:/user  
ENV USER_DIR /user  
# Overall ENV vars  
ARG MESOS_VERSION=1.0.1-2.0.93.debian81  
ARG METRONOME_VERSION=4336d5b15cdd19  
  
ENV PROTOBUF_VERSION=2.6.1-1  
ENV SBT_VERSION=0.13.13  
# Add package sources and install  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo "deb http://repos.mesosphere.io/debian jessie main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \  
apt-get update && \  
apt-get install --no-install-recommends -y --force-yes mesos=$MESOS_VERSION
git sbt=$SBT_VERSION libprotobuf-dev=$PROTOBUF_VERSION protobuf-
compiler=$PROTOBUF_VERSION && \  
mkdir -p $BUILD_DIR && \  
mkdir -p $APP_DIR && \  
mkdir -p $USER_DIR/conf && \  
systemctl disable mesos-master.service && \  
systemctl disable mesos-slave.service && \  
cd $BUILD_DIR && \  
git clone https://github.com/dcos/metronome.git && \  
cd metronome && \  
git checkout -b bb $METRONOME_VERSION && \  
sbt -Dsbt.log.format=false universal:packageBin && \  
mkdir -p /tmp/fake && \  
( find $BUILD_DIR/metronome -iname metronome-\\*.zip | xargs -n 1 -IXX sh -c
"unzip -d /tmp/fake XX; mv /tmp/fake/*/* $APP_DIR/" ) && \  
rm -rf /tmp/fake && \  
rm -rf $BUILD_DIR ~/.sbt ~/.ivy2 ~/.m2 && \  
apt-get purge -y --force-yes git sbt libprotobuf-dev protobuf-compiler && \  
apt-get autoremove -y --force-yes && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
ENV SCALA_MIN_THREADS 5  
ENV SCALA_NUM_THREADS x2  
ENV SCALA_MAX_THREADS 64  
ENV SCALA_OPTS "-Dscala.concurrent.context.minThreads=$SCALA_MIN_THREADS
-Dscala.concurrent.context.numThreads=$SCALA_NUM_THREADS
-Dscala.concurrent.context.maxThreads=${SCALA_MAX_THREADS}"  
CMD $APP_DIR/bin/metronome $JAVA_OPTS $SCALA_OPTS  
  

