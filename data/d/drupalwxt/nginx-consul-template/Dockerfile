# vim:set ft=dockerfile:  
FROM nginx:1.9-alpine  
MAINTAINER William Hearn <sylus1984@gmail.com>  
  
ENV CONSUL_TEMPLATE_VERSION 0.11.0  
RUN apk add --no-cache \  
bash \  
curl \  
jq \  
tar  
  
RUN curl -fSL "https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" -o consul-template.zip \  
&& unzip consul-template.zip \  
&& rm consul-template.zip \  
&& mv consul-template /usr/local/bin \  
&& rm -v /etc/nginx/conf.d/*  
  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/nginx.conf.ctmpl /etc/nginx/nginx.conf.ctmpl  
  
ADD /conf/config.json /scripts/entrypoint.sh /scripts/restart.sh
/scripts/config.sh /  
  
WORKDIR /  
  
EXPOSE 80 443  
CMD ["/entrypoint.sh"]  

