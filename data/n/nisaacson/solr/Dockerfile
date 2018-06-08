# Solr  
#  
# VERSION 0.0.1  
FROM ubuntu:12.10  
MAINTAINER Noah Isaacson noah@nisaacson.com  
  
# Update the APT cache  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update  
RUN locale-gen en_US en_US.UTF-8  
  
# Install and setup project dependencies  
RUN apt-get install -y curl lsb-release supervisor openssh-server build-
essential  
RUN apt-get install -qqy python-software-properties  
RUN apt-get install -qqy vim  
  
RUN mkdir -p /var/log/supervisor  
  
RUN apt-get install -qqy openjdk-7-jre-headless  
RUN wget --progress=bar:force http://mirrored-packages.s3-website-us-
west-1.amazonaws.com/packages/solr-4.2.0.tgz  
RUN tar --extract --file solr-4.2.0.tgz -C /opt  
RUN mv /opt/solr-4.2.0 /opt/solr  
  
# Include basic config  
# Can be override with volume -v flag  
# EX: docker run -v /tmp/solr:/var/lib/solr/solr -p 1111:22 -p 8983:8983 -name
solr-container nisaacson/solr  
ADD ./solr_data /var/lib/solr/solr  
  
# Use supervisor to keep both ssh server and solr java process running  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN echo 'root:root' | chpasswd  
  
# Expose sshd server port  
EXPOSE 22  
# Expose Solr port  
EXPOSE 8983  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

