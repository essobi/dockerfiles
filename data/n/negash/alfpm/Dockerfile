FROM alpine  
WORKDIR /code  
  
# build japronto  
RUN apk add --no-cache python3 ca-certificates  
RUN apk add --no-cache --virtual .build-deps py3-pip \  
&& pip3 install requests apscheduler prometheus-client \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["python3"]  
CMD ["main.py"]  
  
COPY main.py main.py  

