FROM python:2.7  
WORKDIR /code  
  
RUN cd /code \  
&& virtualenv venv \  
&& ./venv/bin/pip install pypicloud[server] uwsgi \  
&& rm /root/.cache -rf \  
&& apt-get update \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
ENV ENV prod  
  
ADD override /  
  
ENTRYPOINT ["bash", "/code/entry.sh"]  

