FROM alpine  
MAINTAINER Oyshik Moitra  
  
ENV SERVICE_NAME consul  
ENV MIN_QUORUM 2  
RUN wget
https://releases.hashicorp.com/consul/1.0.2/consul_1.0.2_linux_amd64.zip \  
&& unzip consul_1.0.2_linux_amd64.zip  
  
RUN apk update \  
&& apk add --no-cache bind-tools bash  
  
ADD docker-entrypoint.sh /  
  
RUN mkdir consul_data && chmod +x docker-entrypoint.sh  
  
EXPOSE 8500  
ENTRYPOINT ["/docker-entrypoint.sh"]

