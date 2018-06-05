FROM httpd:2.4  
MAINTAINER WOW! Group Development  
  
RUN apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install libglib2.0-0 curl unzip \  
&& curl -sSL https://deb.entrouvert.org/entrouvert.gpg | apt-key add - \  
&& echo "deb http://deb.entrouvert.org/ jessie main" >
/etc/apt/sources.list.d/entrouvert.list \  
&& apt-get -y update \  
&& apt-get -y install liblasso3 \  
&& curl -Lo /tmp/cnsltmpl.zip https://releases.hashicorp.com/consul-
template/0.14.0/consul-template_0.14.0_linux_amd64.zip \  
&& unzip /tmp/cnsltmpl.zip -d /usr/local/bin \  
&& chmod +x /usr/local/bin/consul-template \  
&& apt-get -y remove --purge unzip \  
&& apt-get -y autoremove --purge \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/local/apache2/conf/{httpd.conf,extra,original}  
  
ADD runner /  
ADD mod_auth_mellon.so /usr/local/apache2/modules/  
ADD httpd.conf.tmpl /usr/local/apache2/conf/  
  
EXPOSE 8080  
ENTRYPOINT ["/runner"]  
CMD ["httpd-foreground"]  

