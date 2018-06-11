FROM debian:stretch  
  
MAINTAINER Christoph Dwertmann <christoph.dwertmann@vaultsystems.com.au>  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update -qq && \  
apt-get -y install ca-certificates nginx-extras curl runit vim unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
RUN cd /usr/local/bin && curl https://releases.hashicorp.com/consul-
template/0.13.0/consul-template_0.13.0_linux_amd64.zip -o consul.zip && unzip
consul.zip && rm consul.zip  
  
ADD nginx.service /etc/service/nginx/run  
ADD consul-template.service /etc/service/consul-template/run  
ADD conf.d/*.conf /etc/consul-templates/  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD error_pages/* /usr/share/nginx/html/  
  
CMD ["/usr/bin/runsvdir", "/etc/service"]  

