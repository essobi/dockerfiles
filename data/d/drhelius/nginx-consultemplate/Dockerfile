FROM nginx  
  
ENV GIT_SSL_NO_VERIFY=true  
ENV CONSUL_TEMPLATE_VERSION=0.15.0  
ENV CONSUL_URL=consul:8500  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
wget \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -O /tmp/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip --no-check-certificate  
  
RUN unzip /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -d
/usr/local/bin  
  
RUN mkdir /etc/consul-templates  
  
COPY consul.ctmpl /etc/consul-templates/  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY start.sh /bin/start.sh  
  
ENTRYPOINT ["/bin/start.sh"]  

