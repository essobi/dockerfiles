FROM nerc/spark-core:2.1.0.3  
LABEL maintainer "gareth.lloyd@stfc.ac.uk"  
  
ENV ZEPPELIN_VER 0.7.2  
ENV ZEPPELIN_HOME /opt/zeppelin  
ENV ZEPPELIN_USER datalab  
ENV ZEPPELIN_UID 1000  
USER root  
  
# Install Zeppelin  
RUN wget -O /tmp/zeppelin-${ZEPPELIN_VER}-bin-all.tgz
http://archive.apache.org/dist/zeppelin/zeppelin-${ZEPPELIN_VER}/zeppelin-${ZEPPELIN_VER}-bin-
all.tgz && \  
tar -zxvf /tmp/zeppelin-${ZEPPELIN_VER}-bin-all.tgz && \  
rm -rf /tmp/zeppelin-${ZEPPELIN_VER}-bin-all.tgz && \  
mv /zeppelin-${ZEPPELIN_VER}-bin-all ${ZEPPELIN_HOME}  
  
# Add datalab user  
RUN useradd -m -s /bin/bash -N -u $ZEPPELIN_UID $ZEPPELIN_USER && \  
chown -R $ZEPPELIN_USER $ZEPPELIN_HOME && \  
mkdir -p $R_LIBS_SITE_USER && \  
chown -R $ZEPPELIN_USER $R_LIBS_SITE_USER  
  
# Install sudo & GDAL utilities  
RUN apt-get install -y sudo gdal-bin  
  
EXPOSE 8080 8443  
WORKDIR ${ZEPPELIN_HOME}  
  
COPY ./start.sh /usr/local/bin  
COPY ./docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT ["tini", "--"]  
CMD ["start.sh", "docker-entrypoint.sh"]  
  
USER $ZEPPELIN_USER  

