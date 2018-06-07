FROM centos:centos7  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk  
  
# Install Java and the "which" command, which is needed by ES's shell scripts.  
RUN yum install -y java-1.8.0-openjdk-headless unzip which && \  
yum clean all  
  
# Provide a non-root user to run the process.  
RUN groupadd -g 1000 elasticsearch && \  
adduser -u 1000 -g 1000 -d /usr/share/elasticsearch elasticsearch  
  
WORKDIR /usr/share/elasticsearch  
  
USER 1000  
ENV URL_ROOT https://artifacts.elastic.co/downloads/elasticsearch  
ENV TARBALL elasticsearch-6.2.3.tar.gz  
  
# Download and extract defined elasticsearch version.  
RUN curl -fsSL ${URL_ROOT}/${TARBALL}| \  
tar zx --strip-components=1  
  
RUN set -ex && for esdirs in config data logs; do \  
mkdir -p "$esdirs"; \  
done  
  
USER 0  
# Provide a minimal configuration  
ADD config/ config/  
  
# Set gid to 0 for elasticsearch and make group permission similar to that of
user  
RUN chown -R elasticsearch:0 . && \  
chmod -R g=u /usr/share/elasticsearch  
  
RUN chmod 0775 /usr/share/elasticsearch && \  
chgrp 0 /usr/share/elasticsearch  
  
# Expose ports  
EXPOSE 9200 9300  
# Switch to the user 185 for OpenShift usage  
USER 185  
CMD [ "/usr/share/elasticsearch/bin/elasticsearch" ]  
  

