FROM python:2.7  
MAINTAINER unknownlighter@gmail.com  
  
RUN apt-get update && apt-get install -y \  
nginx \  
gdal-bin \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /server  
  
COPY requirements.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
COPY nginx.conf /etc/nginx/sites-enabled/default  
  
ADD . .  
  
RUN mkdir /files  
  
EXPOSE 80  
CMD nginx && python server.py --port 8000 --save-dir /files/ --save-dir-url
${SERVER_URL}/files/  

