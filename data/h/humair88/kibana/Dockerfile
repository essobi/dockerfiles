FROM centos:centos7  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk  
  
# Install Java and the "which" command, which is needed by Logstash's shell
scripts.  
RUN yum install -y fontconfig freetype && \  
yum clean all  
  
# Provide a non-root user to run the process.  
RUN groupadd -g 1000 kibana && \  
adduser -u 1000 -g 1000 -d /usr/share/kibana kibana  
  
WORKDIR /usr/share/kibana  
  
# Download and extract defined kibana version.  
ENV URL_ROOT https://artifacts.elastic.co/downloads/kibana  
ENV TARBALL kibana-6.2.4-linux-x86_64.tar.gz  
  
# Download and extract defined ES version.  
RUN curl -fsSL ${URL_ROOT}/${TARBALL}| \  
tar zx --strip-components=1  
  
# Provide a minimal configuration  
ADD config/ config/  
  
# Set gid to 0 for elasticsearch and make group permission similar to that of
user  
WORKDIR /usr/share  
RUN chown -R kibana:0 kibana && \  
chmod -R g=u kibana  
  
# Expose ports  
EXPOSE 5601  
# Switch to the user 185 for OpenShift usage  
USER 185  
CMD [ "/usr/share/kibana/bin/kibana" ]

