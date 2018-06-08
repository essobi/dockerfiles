FROM ubuntu  
  
RUN apt-get update; \  
apt-get upgrade -y  
RUN apt-get install -y \  
nginx \  
letsencrypt \  
python-pip \  
python  
  
RUN service nginx stop  
COPY config/supervisord.conf /etc/supervisord.conf  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
RUN pip install --upgrade pip  
RUN pip install supervisor  
RUN pip install supervisor-stdout  
  
WORKDIR /proxy  
COPY . .  
RUN pip install -r requirements.txt  
EXPOSE 80  
EXPOSE 443  
CMD /usr/local/bin/supervisord -c /etc/supervisord.conf -n

