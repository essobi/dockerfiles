FROM java:8  
  
RUN mkdir -p /opt/druid  
WORKDIR /opt/druid  
RUN curl -O http://static.druid.io/artifacts/releases/druid-0.11.0-bin.tar.gz  
RUN tar -xzf druid-0.11.0-bin.tar.gz  
RUN ln -sf druid-0.11.0 current  
  
WORKDIR /opt/druid/current  
  
RUN mkdir log && \  
mkdir -p var/tmp && \  
mkdir -p var/druid/indexing-logs && \  
mkdir -p var/druid/segments && \  
mkdir -p var/druid/segment-cache && \  
mkdir -p var/druid/task && \  
mkdir -p var/druid/hadoop-tmp && \  
mkdir -p var/druid/pids && \  
mkdir -p _config/common && \  
mkdir -p _config/specific  
  
RUN java -classpath "lib/*" io.druid.cli.Main tools \  
pull-deps \  
\--no-default-hadoop \  
-c io.druid.extensions:mysql-metadata-storage:0.11.0 \  
-c io.druid.extensions.contrib:kafka-emitter  

