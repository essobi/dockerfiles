FROM nginx:1.9.14  
MAINTAINER Cheng Long <me@chengl.com>  
  
RUN apt-get update && apt-get install -y unzip  
  
ENTRYPOINT ["/bin/start.sh"]  
EXPOSE 80  
ENV CONSUL_URL consul:8500  
COPY start.sh /bin/start.sh  
RUN chmod +x /bin/start.sh  
COPY service.ctmpl /templates/service.ctmpl  
  
ADD https://releases.hashicorp.com/consul-template/0.14.0/consul-
template_0.14.0_linux_amd64.zip /tmp  
RUN unzip /tmp/consul-template_0.14.0_linux_amd64.zip -d /usr/local/bin  
  

