FROM rodrigozc/consul:1.0.2  
LABEL author.name="Rodrigo Zampieri Castilho"  
LABEL author.email="rodrigo.zampieri@gmail.com"  
LABEL repository.url="https://bitbucket.org/rcastilho/rabbitmq"  
  
ENV APPLICATION_DEFAULT_NAME "rabbitmq"  
ENV RABBITMQ_DEFAULT_USER "guest"  
ENV RABBITMQ_DEFAULT_PASS "guest"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends gnupg2 \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
RUN mkdir -p /docker/rabbitmq/setup \  
&& echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee
/etc/apt/sources.list.d/rabbitmq.list \  
&& wget --no-check-certificate -O- https://www.rabbitmq.com/rabbitmq-release-
signing-key.asc | apt-key add - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends rabbitmq-server \  
&& rabbitmq-plugins enable \--offline rabbitmq_management \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
ADD /etc/rabbitmq/rabbitmq.config /etc/rabbitmq/  
ADD /etc/default/rabbitmq-server /etc/default/  
ADD consul-template/1-consul-template.list /etc/consul-template/  
ADD consul/service.ctmpl /etc/consul/  
ADD consul/service.json /etc/consul/  
ADD run/rabbitmq.sh /docker/run/  

