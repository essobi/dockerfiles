FROM debian  
  
MAINTAINER Olivier Sallou <olivier.sallou@irisa.fr>  
  
RUN apt-get update  
RUN apt-get install -y vim wget unzip lsb-release gnupg2  
RUN wget -O - https://nginx.org/keys/nginx_signing.key | apt-key add -  
RUN echo "deb http://nginx.org/packages/debian/ $(lsb_release -sc) nginx" >
/etc/apt/sources.list.d/nginx.list  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN wget https://releases.hashicorp.com/consul-template/0.16.0/consul-
template_0.16.0_linux_amd64.zip  
RUN unzip consul-template_0.16.0_linux_amd64.zip && rm consul-
template_0.16.0_linux_amd64.zip  
RUN echo "#!/bin/bash\nservice nginx start && /consul-template -consul biomaj-
consul:8500 -template \"/proxy/nginx.ctmpl:/etc/nginx/nginx.conf:service nginx
reload\" -retry 30s" > /nginx-template.sh  
RUN chmod 755 /nginx-template.sh  
COPY status /usr/share/nginx/html/status  
ENTRYPOINT ["/nginx-template.sh"]  

