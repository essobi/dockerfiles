FROM datadog/docker-dd-agent  
MAINTAINER Saúl Hernández <saul.hernandez@synergy-gb.com>  
  
RUN apt-get update  
RUN apt-get install curl -y  
  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 -o /bin/confd  
  
RUN chmod +x /bin/confd  
  
RUN mkdir -p /etc/confd/  
ADD conf.d /etc/confd/conf.d  
ADD templates /etc/confd/templates  
  
ADD confd-watch /bin/confd-watch  
RUN chmod +x /bin/confd-watch  
  
ENTRYPOINT ["/bin/confd-watch"]  
CMD []  

