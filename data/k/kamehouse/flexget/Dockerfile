FROM python:3.5  
MAINTAINER Michael Baudino <michael.baudino@alpine-lab.com>  
  
RUN pip install -I flexget transmissionrpc  
  
RUN mkdir -p /flexget /etc/flexget  
COPY config.template.yml /etc/flexget/config.template.yml  
  
WORKDIR /flexget  
  
COPY flexget-config-replacer /usr/local/bin  
  
ENTRYPOINT ["flexget-config-replacer"]  
CMD ["flexget", "--loglevel", "verbose", "-c", "/flexget/config.yml",
"daemon", "start"]  

