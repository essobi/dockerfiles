FROM zingsono/centos:7  
MAINTAINER Zengs.<zingsono@gmail.com>  
  
WORKDIR /kibana  
  
ENV KIBANA_VERSION=6.2.4  
RUN curl -o kibana.tar.gz
"https://artifacts.elastic.co/downloads/kibana/kibana-$KIBANA_VERSION-
linux-x86_64.tar.gz" && tar -xf kibana.tar.gz --strip-components=1 && rm -f
kibana.tar.gz  
ENV PATH=$PATH:/kibana/bin/  
  
# 配置文件: /kibana/config/kibana.yml  
VOLUME /kibana/  
  
EXPOSE 5601  
CMD ["kibana"]

