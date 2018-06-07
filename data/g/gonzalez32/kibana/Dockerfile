FROM centos:7  
LABEL maintainer "Elastic Docker Team <docker@elastic.co>"  
EXPOSE 5601  
ARG ELASTIC_VERSION=5.6.3  
ARG
URL_ROOT=https://artifacts.elastic.co/downloads/kibana/kibana-${ELASTIC_VERSION}  
  
# Add Reporting dependencies.  
RUN yum update -y && yum install -y fontconfig freetype && yum clean all  
  
WORKDIR /usr/share/kibana  
RUN curl -Ls ${URL_ROOT}-linux-x86_64.tar.gz | tar --strip-components=1 -zxf -
&& \  
ln -s /usr/share/kibana /opt/kibana  
  
ENV ELASTIC_CONTAINER true  
ENV PATH=/usr/share/kibana/bin:$PATH  
  
# Set some Kibana configuration defaults.  
ADD config/kibana.yml /usr/share/kibana/config/  
  
# Add the launcher/wrapper script. It knows how to interpret environment  
# variables and translate them to Kibana CLI options.  
ADD bin/kibana-docker /usr/share/kibana/bin/  
RUN chmod +x /usr/share/kibana/bin/kibana-docker  
  
# Add a self-signed SSL certificate for use in examples.  
ADD ssl/kibana.example.org.* /usr/share/kibana/config/  
  
# Provide a non-root user to run the process.  
RUN groupadd --gid 1000 kibana && \  
useradd --uid 1000 --gid 1000 \  
\--home-dir /usr/share/kibana --no-create-home \  
kibana  
USER kibana  
  
#RUN kibana-plugin install x-pack  
ENTRYPOINT ["/usr/share/kibana/bin/kibana-docker"]  
  

