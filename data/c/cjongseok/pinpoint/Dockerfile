FROM cjongseok/oracle-jdk:1.8.0_77  
MAINTAINER Jongseok Choi <cjongseok@gmail.com>  
  
ENV HBASE_DOCKER_HOME /opt/hbase  
  
RUN set -e \  
&& set -x \  
&& apt-get install -y wget curl \  
&& mkdir -p ${HBASE_DOCKER_HOME}  
  
COPY conf ${HBASE_DOCKER_HOME}/conf  
COPY scripts ${HBASE_DOCKER_HOME}/scripts  
  
RUN set -e \  
&& set -x \  
&& /bin/bash -c "set -e && set -x && source
${HBASE_DOCKER_HOME}/scripts/start-hbase.sh && func_install_hbase"  
  
WORKDIR ${HBASE_DOCKER_HOME}  
  
CMD ["scripts/run.sh"]  

