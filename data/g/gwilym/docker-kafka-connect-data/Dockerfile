# Kafka Connect pre-packaged with all the connectors we need  
  
FROM confluentinc/cp-kafka-connect:5.0.0-beta30-1  
  
ENV RUNTIME_PIP_PACKAGES="awscli"  
  
RUN pip install --upgrade $RUNTIME_PIP_PACKAGES \  
&& aws --version \  
  
&& sed -ie 's/^#networkaddress.cache.ttl=-1$/networkaddress.cache.ttl=30/'
/usr/lib/jvm/zulu-8-amd64/jre/lib/security/java.security \  
  
&& apt-get -qy autoremove --purge \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY include/etc/confluent/docker /etc/confluent/docker  
COPY include/etc/bigcommerce /etc/bigcommerce  

