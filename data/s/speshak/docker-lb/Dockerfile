FROM nginx  
  
MAINTAINER Scott Peshak <scott@peshak.net>  
RUN apt-get update -qq && apt-get install -y curl  
  
ENV DL_URL https://releases.hashicorp.com/consul-template/0.18.0/consul-
template_0.18.0_linux_amd64.tgz  
RUN curl -sSL $DL_URL | tar -C /usr/local/bin --strip-components 1 -zxf -  
  
ADD nginx.service /etc/service/nginx/run  
ADD consul-template.service /etc/service/consul-template/run  
RUN find /etc/service -type f -name 'run' -a ! -executable -exec chmod +x {}
\;  
  
RUN rm -v /etc/nginx/conf.d/*  
ADD nginx.conf /etc/nginx/nginx.conf  
  
VOLUME /etc/consul-templates  
  
ADD app.conf.ctmpl /etc/consul-templates/app.conf.ctmpl  
  
CMD ["my_init"]  
  
# Clean up APT  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

