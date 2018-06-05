FROM python:2.7-alpine  
  
RUN apk --no-cache add curl bash  
  
RUN curl -s -f -L -o schema-tool.tar.gz https://github.com/appnexus/schema-
tool/archive/0.3.0.tar.gz \  
&& tar xzvf schema-tool.tar.gz  
  
WORKDIR "/app"  
ENTRYPOINT ["/schema-tool-0.3.0/schema"]  
CMD ["help"]  

