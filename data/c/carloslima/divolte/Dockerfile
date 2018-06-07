FROM anapsix/alpine-java:8_server-jre  
  
ENV divolte_version 0.5.0  
RUN wget -O- http://divolte-releases.s3-website-eu-
west-1.amazonaws.com/divolte-collector/$divolte_version/distributions/divolte-
collector-$divolte_version.tar.gz | tar xzf - -C /opt  
  
RUN mv /opt/divolte-collector-* /opt/divolte \  
&& sed -E 's|(\s*)//\s*host\s*= |\1host = |' /opt/divolte/conf/divolte-
collector.conf.example > /opt/divolte/conf/divolte-collector.conf  
  
ENV JAVA_HOME /opt/jdk/  
ENV DIVOLTE_HOST 0.0.0.0  
EXPOSE 8290  
WORKDIR /opt/divolte  
ENTRYPOINT ["/opt/divolte/bin/divolte-collector"]  

