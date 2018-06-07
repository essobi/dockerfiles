FROM centos:centos7  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk  
  
# Install Java and the "which" command, which is needed by Logstash's shell
scripts.  
RUN yum install -y java-1.8.0-openjdk-headless unzip which && \  
yum clean all  
  
# Provide a non-root user to run the process.  
RUN groupadd -g 1000 logstash && \  
adduser -u 1000 -g 1000 -d /usr/share/logstash logstash  
  
WORKDIR /usr/share/logstash  
  
ENV URL_ROOT https://artifacts.elastic.co/downloads/logstash  
ENV TARBALL logstash-6.2.4.tar.gz  
  
# Download and extract defined logstash version.  
RUN curl -fsSL ${URL_ROOT}/${TARBALL}| \  
tar zx --strip-components=1  
  
ENV ELASTIC_CONTAINER true  
ENV PATH=/usr/share/logstash/bin:$PATH  
  
# Provide a minimal configuration  
ADD config/ config/  
RUN chown --recursive logstash:logstash config/  
  
# Ensure Logstash gets a UTF-8 locale by default.  
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
# Set gid to 0 for elasticsearch and make group permission similar to that of
user  
WORKDIR /usr/share  
RUN chown -R logstash:0 logstash && \  
chmod -R g=u logstash  
  
# Expose ports  
EXPOSE 9600 5044  
# Switch to the user 185 for OpenShift usage  
USER 185  
CMD [ "/usr/share/logstash/bin/logstash" ]

