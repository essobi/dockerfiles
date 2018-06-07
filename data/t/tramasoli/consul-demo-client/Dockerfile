FROM tramasoli/sample-springboot-rest  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
LABEL env=des  
RUN apt-get update \  
&& apt-get install unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* \  
&& cd /usr/local/bin \  
&& wget
https://releases.hashicorp.com/consul/0.7.1/consul_0.7.1_linux_amd64.zip \  
&& unzip consul*zip \  
&& rm consul*zip \  
&& mkdir -p /consul/data \  
&& mkdir -p /consul/config  
  
RUN echo "/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -jar /tmp/sample-
springboot-rest/gs-rest-service-complete/target/*jar & " > /bootstrap.sh  
RUN echo "/usr/local/bin/consul agent -data-dir=/consul/data -config-
dir=/consul/config " >> /bootstrap.sh  
VOLUME /consul/config  
EXPOSE 8500 8080  
CMD ["/bin/bash","/bootstrap.sh"]  

