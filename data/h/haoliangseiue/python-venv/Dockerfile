FROM python:3-slim  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
mime-support \  
python3-venv \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

