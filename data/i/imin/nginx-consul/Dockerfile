FROM nginx:latest  
  
ADD http://releases.hashicorp.com/consul-template/0.15.0/consul-
template_0.15.0_linux_amd64.zip /var/tmp/  
RUN apt-get -qq update && apt-get -qq install unzip  
RUN unzip -d /usr/local/bin /var/tmp/consul-template_0.15.0_linux_amd64.zip  
  
RUN rm -v /etc/nginx/conf.d/*.conf  
  
ADD nginx.hcl /etc/consul-template.d/  
  
VOLUME /templates  
ADD nginx-consul.ctmpl /templates/  
  
EXPOSE 80  
ENTRYPOINT ["consul-template","-config=/etc/consul-template.d"]  
CMD ["-consul=consul-8500.service.consul:8500"]  

