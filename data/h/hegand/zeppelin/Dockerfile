FROM hegand/spark-base:1.6-hadoop-full-stack-2.7  
ENV ZEPPELIN_VERSION 0.7.0  
ENV ZEPPELIN_FULL_VERSION zeppelin-${ZEPPELIN_VERSION}  
ENV ZEPPELIN_HOME /usr/local/zeppelin  
ENV PATH $PATH:$ZEPPELIN_HOME/bin  
  
RUN adduser -D -s /bin/bash -u 1210 zeppelin  
  
RUN set -x && \  
mkdir -p /usr/local && \  
cd /tmp && \  
wget -q
http://apache.claz.org/zeppelin/${ZEPPELIN_FULL_VERSION}/${ZEPPELIN_FULL_VERSION}-bin-
netinst.tgz -O - | tar -xz && \  
mv ${ZEPPELIN_FULL_VERSION}-bin-netinst /usr/local && \  
ln -s /usr/local/${ZEPPELIN_FULL_VERSION}-bin-netinst ${ZEPPELIN_HOME} && \  
chown -R zeppelin:zeppelin ${ZEPPELIN_HOME}/  
  
RUN ${ZEPPELIN_HOME}/bin/install-interpreter.sh --name md,shell,jdbc,python  
  
WORKDIR ${ZEPPELIN_HOME}  

