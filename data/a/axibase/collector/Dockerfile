FROM ubuntu:16.04  
ENV version=19344 LANG=en_US.UTF-8  
#metadata  
LABEL maintainer="ATSD Developers <dev-atsd@axibase.com>" \  
com.axibase.vendor="Axibase Corporation" \  
com.axibase.product="Axibase Collector" \  
com.axibase.code="AC" \  
com.axibase.revision="${version}"  
  
#entrypoint script  
COPY entrypoint.sh preinit.sh /tmp/  
  
#install jre, cron, collector, explode (unpack) war file to speed up inital
startup  
RUN apt-get update && apt-get install --no-install-recommends -y openjdk-8-jdk
wget unzip cron nano iproute2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://www.axibase.com/public/axibase-collector-v${version}.tar.gz \  
&& tar -xzvf axibase-collector-*.tar.gz -C /opt/ && rm axibase-
collector-*.tar.gz \  
&& mkdir -p /opt/axibase-collector/exploded/webapp \  
&& unzip /opt/axibase-collector/lib/axibase-collector.war -d /opt/axibase-
collector/exploded/webapp \  
&& mv /tmp/entrypoint.sh /opt/axibase-collector/bin/ \  
&& /tmp/preinit.sh  
  
#expose UI https port  
EXPOSE 9443  
VOLUME ["/opt/axibase-collector"]  
  
ENTRYPOINT ["/bin/bash","/opt/axibase-collector/bin/entrypoint.sh"]  

