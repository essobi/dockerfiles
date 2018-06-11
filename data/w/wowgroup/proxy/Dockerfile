FROM nginx  
MAINTAINER WOW! Group Development  
  
ADD runner /  
RUN apt-get -y update \  
&& apt-get -y install curl unzip \  
&& curl -sSL -o /tmp/cnsltmpl.zip https://releases.hashicorp.com/consul-
template/0.15.0/consul-template_0.15.0_linux_amd64.zip \  
&& unzip /tmp/cnsltmpl.zip -d /usr/local/bin \  
&& chmod +x /usr/local/bin/consul-template \  
&& apt-get -y remove --purge curl unzip \  
&& apt-get -y autoremove --purge \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/nginx/nginx.conf
/etc/nginx/conf.d/* \  
&& chmod +x /runner  
  
ADD nginx.conf.tmpl http.conf /etc/nginx/  
  
EXPOSE 8080 8081  
CMD ["/runner"]  

