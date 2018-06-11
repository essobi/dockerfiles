# As the integrated `node` binary inside 'zeppelin' are dynamically linked to
/lib64/, it cannot use Alpine image for now  
FROM openjdk:8-jdk-slim  
  
ENV ZEPPELIN_HOME /opt/zeppelin  
ENV PATH=$PATH:${ZEPPELIN_HOME}/bin  
EXPOSE 8080  
RUN groupadd -r --gid 501 zeppelin \  
&& useradd -r --uid 501 --home-dir ${ZEPPELIN_HOME} \--create-home -g zeppelin
zeppelin  
  
WORKDIR ${ZEPPELIN_HOME}  
  
# For Alpine  
# RUN apk --no-cache add bash  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/list/*  
  
ENV ZEPPELIN_DATA /data  
ENV ZEPPELIN_LOG_DIR ${ZEPPELIN_DATA}/log  
ENV ZEPPELIN_PID_DIR ${ZEPPELIN_DATA}/run  
ENV ZEPPELIN_NOTEBOOK_DIR ${ZEPPELIN_DATA}/notebook  
  
# Prepare the permission for the mount points  
RUN mkdir -p ${ZEPPELIN_DATA} && chown zeppelin:zeppelin ${ZEPPELIN_DATA}  
VOLUME ${ZEPPELIN_DATA}  
  
# Let temporary directories to be volumes as well  
VOLUME /tmp  
  
USER zeppelin  
  
ENV ZEPPELIN_VERSION 0.7.2  
RUN set -xe \  
&& cd /tmp \  
&& wget
http://www.apache.org/dist/zeppelin/zeppelin-${ZEPPELIN_VERSION}/zeppelin-${ZEPPELIN_VERSION}-bin-
netinst.tgz \  
&& tar -zxvf zeppelin-${ZEPPELIN_VERSION}-bin-netinst.tgz -C ${ZEPPELIN_HOME}
\--strip-components=1 \  
&& rm *.tgz  
  
# We don't need that much memory for interpreter installation  
RUN set -xe \  
&& mkdir -p ${ZEPPELIN_LOG_DIR} \  
&& export ZEPPELIN_MEM='-Xmx256m' \  
&& install-interpreter.sh --list && install-interpreter.sh --name
angular,python,shell,bigquery,file,jdbc,kylin,livy,md,postgresql  
  
CMD ["zeppelin.sh"]  

