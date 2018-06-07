FROM maven:3.5.2-jdk-8  
MAINTAINER D.Valocchi <d.valocchi@ucl.ac.uk>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
netcat  
  
ADD adaptor /adaptor  
ADD broker.config /etc/son-mano/broker.config  
ADD postgres.config /etc/son-mano/postgres.config  
ADD mistral.config /etc/son-mano/mistral.config  
ADD sonata.config /etc/son-mano/sonata.config  
  
ADD son-sp-infra-* /usr/local/bin/  
ADD son-sp-infra /etc/init.d/  
ADD ./setenv.sh /  
ADD ./test.sh /  
ADD ./docker-entrypoint.sh /  
ADD ./terraform.sh /  
RUN chmod +x /setenv.sh  
RUN chmod +x /test.sh  
RUN chmod +x /usr/local/bin/son-sp-infra-*  
RUN chmod +x /etc/init.d/son-sp-infra  
RUN chmod +x /terraform.sh  
RUN ./terraform.sh  
  
WORKDIR /adaptor  
  
ENV broker_host broker  
ENV broker_port 5672  
ENV broker_exchange son-kernel  
ENV broker_uri amqp://guest:guest@broker:5672/%2F  
  
ENV repo_host postgres  
ENV repo_port 5432  
ENV repo_user sonatatest  
ENV repo_pass sonata  
ENV SONATA_SP_ADDRESS 127.0.0.1  
ENV SONATA_2ND_SP_ADDRESS 127.0.0.1  
ENV MOCKED_2ND_PLATFORM true  
  
ENV mistral_server mistral  
  
RUN mvn -e -q compile assembly:single;  
  
CMD ["/docker-entrypoint.sh","/test.sh"]  
  

