FROM nginx:latest  
  
ENV CONSUL_TEMPLATE_VERSION 0.11.0  
ENV CONSUL_URL consul:8500  
ADD start.sh /bin/start.sh  
RUN rm -v /etc/nginx/conf.d/*.conf  
  
ADD https://github.com/hashicorp/consul-
template/releases/download/v${CONSUL_TEMPLATE_VERSION}/consul_template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip
/tmp/consul-template.zip  
  
RUN apt-get update && apt-get install unzip -y && \  
unzip -j -d /usr/local/bin /tmp/consul-template.zip  
  
EXPOSE 8080 9995 9996  
VOLUME /templates  
  
CMD ["/bin/start.sh"]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

