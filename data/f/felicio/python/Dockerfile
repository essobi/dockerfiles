FROM alpine  
  
RUN apk add --no-cache python3 \  
&& ln -s /usr/bin/python3 /usr/bin/python  
  
RUN pip3 install --upgrade --no-cache-dir pip  
  
ENTRYPOINT ["python"]  

