FROM binhnv/openjdk  
MAINTAINER "Binh Van Nguyen<binhnv80@gmail.com>"  
# Storm UI, logviewer and nimbus thrift ports  
EXPOSE 8080 8000 6627  
ENV STORM_NIMBUS_HOST="\"localhost\"" \  
STORM_HOME="${MY_APP_DIR}/storm" \  
STORM_LOG_DIR="${MY_APP_LOG_DIR}/storm" \  
STORM_LOCAL_DIR="${MY_APP_DATA_DIR}/storm" \  
STORM_DISTRO_NAME="apache-storm-0.10.2" \  
STORM_SUPERVISOR_SLOTS_PORTS="6701,6702,6703,6704" \  
STORM_WORKER_CHILDOPTS="-Xmx512m -XX:ParallelGCThreads=1
-Djava.net.preferIPv4Stack=true" \  
STORM_WORKER_GC_CHILDOPTS="-XX:+UseConcMarkSweepGC -XX:+UseParNewGC" \  
STORM_SUPERVISOR_CHILDOPTS="-Xmx512m" \  
STORM_NIMBUS_CHILDOPTS="-Xmx512m" \  
STORM_UI_CHILDOPTS="-Xmx128m" \  
STORM_NIMBUS_THRIFT_MAX_BUFFER_SIZE="1048576"  
# User need to provide the following environment variables  
# - ZOOKEEPER_HOST: Zookeeper hostname in format of "zk1","zk2"  
WORKDIR ${STORM_HOME}  
COPY scripts/build /my_build  
RUN /my_build/install.sh && rm -rf /my_build  
  
COPY templates ${MY_TEMPLATE_DIR}  
COPY scripts/my_storm /sbin/my_storm  

