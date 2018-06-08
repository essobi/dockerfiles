from nginx  
  
ENV CT=/opt/consul-template  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update -qq && \  
apt-get -y install curl unzip runit && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://releases.hashicorp.com/consul-template/0.12.0/consul-
template_0.12.0_linux_amd64.zip > /tmp/consul-template_0.12.0_linux_amd64.zip  
  
RUN mkdir -p $CT/bin $CT/etc $CT/templates  
RUN cd $CT/bin && unzip /tmp/consul-template_0.12.0_linux_amd64.zip  
  
ADD *.ctmpl $CT/templates/  
ADD consul-template.conf $CT/etc/  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
ADD nginx-reload.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/nginx-reload.sh  
  
ADD run.sh /  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  
  

