FROM php:7.1  
MAINTAINER Vadim Slizov <z7zmey@gmail.com>  
  
RUN echo 'deb http://apt.vandenbrand.org/debian testing main' >>
/etc/apt/sources.list  
  
RUN curl -o /tmp/apt.vandenbrand.org.gpg.key
http://apt.vandenbrand.org/apt.vandenbrand.org.gpg.key \  
&& apt-key add /tmp/apt.vandenbrand.org.gpg.key \  
&& apt-get update \  
&& apt-get install rabbitmq-cli-consumer  
  
ADD ./configuration.conf /etc/rabbitmq-cli-consumer/config.conf  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD rabbitmq-cli-consumer -c /etc/rabbitmq-cli-consumer/config.conf -V

