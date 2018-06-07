FROM python:3.6-alpine  
  
RUN apk add --no-cache --virtual .build-deps g++ linux-headers make \  
&& apk add --no-cache libxml2-dev libxslt-dev \  
&& pip install hovercraft==2.4 \  
&& apk del .build-deps \  
&& mkdir -p /presentation  
  
WORKDIR /presentation  
EXPOSE 9000  
ENTRYPOINT ["hovercraft", "--port", "0.0.0.0:9000"]  
CMD ["/presentation"]  

