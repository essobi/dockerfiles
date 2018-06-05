FROM debian:8  
ADD . /arts  
WORKDIR /arts  
RUN echo "Installing python requirements"; mkdir run results upload; apt-get
update; apt-get install -y python-pip python-dev libjpeg-dev libfreetype6-dev
zlib1g-dev; \  
printf "uwsgi" >> requirements.txt && pip install -r requirements.txt && rm
config/artsapp_default.conf && \  
cat config/artsapp_docker.conf | sed "s/PASTE-KEY-HERE/$(openssl rand -base64
32 | tr -dc _a-z-A-Z-0-9)/g" > config/artsapp_default.conf;  
CMD ["uwsgi","--ini","config/uwsgi_docker.conf"]  

