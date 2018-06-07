FROM java:7-jre  
MAINTAINER Piyush Mattoo <Piyush.Mattoo@software.dell.com> (@pmattoo)  
  
# Download Doradus logstash  
ENV LOGSTASH_HOME /opt/logstash  
ENV LOGSTASH_VERSION='1.5.0'  
ENV LOGSTASH_NAME="logstash-${LOGSTASH_VERSION}"  
ENV LOGSTASH_URL="https://git.labs.dell.com/projects/BD/repos/logstash-output-
batched_http/browse/artifacts/${LOGSTASH_NAME}.tar.gz?raw"  
RUN mkdir ${LOGSTASH_HOME} && \  
cd ${LOGSTASH_HOME} && \  
wget https://git.labs.dell.com/projects/BD/repos/logstash-output-
batched_http/browse/artifacts/logstash-1.5.0.tar.gz?raw && \  
tar -xzf logstash-1.5.0.tar.gz?raw && \  
mv ${LOGSTASH_NAME} logstash && \  
rm logstash-1.5.0.tar.gz?raw  
  
# Add the script to run docker-doradus-logstash  
ADD docker-doradus-logstash.sh /usr/bin/  
RUN chmod a+x /usr/bin/docker-doradus-logstash.sh  
  
# Any docker logs need to be mounted at /host/var/log. Typically, this means
that  
# a volume should be created mapping /var/lib/docker/containers to
/host/var/log  
# in the container.  
VOLUME ["/host/var/log"]  
  
RUN mkdir /var/log/logstash  
RUN mkdir ${LOGSTASH_HOME}/conf.d  
ADD logstash.conf ${LOGSTASH_HOME}/conf.d/  
  
#ENTRYPOINT ["/usr/bin/docker-doradus-logstash.sh"]  
#CMD ["agent"]

