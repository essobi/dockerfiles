FROM nginx:alpine  
  
MAINTAINER Paul Beswick  
  
ENV CONSUL_TEMPLATE_VERSION 0.14.0  
ENV CT_FILE /consul-template/templates/nginx.conf.ctmpl  
ENV NX_FILE /etc/nginx/nginx.conf  
  
RUN apk add --update curl jq gettext unzip  
  
# Install consul template  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /  
RUN unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -d
/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64 && \  
mv consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64/consul-template
/usr/local/bin/consul-template &&\  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64 && \  
mkdir -p /consul-template /consul-template/config.d /consul-template/templates  
  
ADD nginx.conf /etc/nginx/nginx-template.conf  
ADD nginx.conf.ctmpl /consul-template/templates/nginx.conf.ctmpl  
ADD entrypoint.sh entrypoint.sh  
RUN chmod +x entrypoint.sh  
  
CMD ["/bin/sh", "entrypoint.sh"]  

