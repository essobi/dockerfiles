  
FROM centos:7  
LABEL maintainer "Cailen <cailen@me.com>"  
EXPOSE 5601  
# Add Reporting dependencies.  
RUN yum update -y && yum install -y fontconfig freetype && yum clean all  
  
WORKDIR /usr/share/kibana  
RUN curl -Ls
https://artifacts.elastic.co/downloads/kibana/kibana-6.1.2-linux-x86_64.tar.gz
| tar --strip-components=1 -zxf - && \  
ln -s /usr/share/kibana /opt/kibana  
  
ENV PATH=/usr/share/kibana/bin:$PATH  
ENV ELASTIC_CONTAINER=true \  
CONSOLE_ENABLED=false \  
XPACK_APM_ENABLED=false \  
XPACK_ML_ENABLED=false \  
XPACK_GRAPH_ENABLED=false \  
XPACK_GROKDEBUGGER_ENABLED=false \  
XPACK_SECURITY_ENABLED=false  
  
# Set some Kibana configuration defaults.  
COPY config/kibana.yml /usr/share/kibana/config/kibana.yml  
  
# Add the launcher/wrapper script. It knows how to interpret environment  
# variables and translate them to Kibana CLI options.  
COPY bin/kibana-docker /usr/local/bin/  
  
# Provide a non-root user to run the process.  
RUN groupadd --gid 1000 kibana && \  
useradd --uid 1000 --gid 1000 \  
\--home-dir /usr/share/kibana --no-create-home \  
kibana  
USER kibana  
  
RUN kibana-plugin install x-pack  
RUN kibana-plugin install
https://github.com/sirensolutions/sentinl/releases/download/tag-6.2.2/sentinl-v6.1.2.zip  
  
CMD ["/bin/bash", "/usr/local/bin/kibana-docker"]  

