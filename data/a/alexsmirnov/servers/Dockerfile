FROM alexsmirnov/servers:spark-2.0.2  
MAINTAINER alexsmirnov  
  
ENV zeppelin_ver 0.6.2  
ENV ZEPPELIN_HOME /opt/zeppelin  
ENV ZEPPELIN_CONF_DIR "${ZEPPELIN_HOME}/conf"  
ENV MASTER "spark://spark-master:7077"  
ENV ZEPPELIN_NOTEBOOK_DIR "${ZEPPELIN_HOME}/notebook"  
ENV ZEPPELIN_MEM -Xmx1024m  
  
RUN apt-get update && apt-get install -y python-matplotlib && rm -rf
/var/lib/apt/lists/* \  
&& curl
http://mirrors.ibiblio.org/apache/zeppelin/zeppelin-${zeppelin_ver}/zeppelin-${zeppelin_ver}-bin-
netinst.tgz | \  
tar -zx -C /opt \  
&& ln -s /opt/zeppelin-${zeppelin_ver}-bin-netinst ${ZEPPELIN_HOME} \  
&& ${ZEPPELIN_HOME}/bin/install-interpreter.sh --name md,python,shell,file  
  
COPY zeppelin-log4j.properties ${ZEPPELIN_HOME}/conf/log4j.properties  
COPY zeppelin-env.sh ${ZEPPELIN_HOME}/conf/zeppelin-env.sh  
COPY docker-zeppelin.sh ${ZEPPELIN_HOME}/bin/docker-zeppelin.sh  
  
ENV MATPLOTLIBRC "${ZEPPELIN_HOME}/conf"  
COPY matplotlibrc ${ZEPPELIN_HOME}/conf/matplotlibrc  
EXPOSE 8080  
ENTRYPOINT ["/opt/zeppelin/bin/docker-zeppelin.sh"]  

