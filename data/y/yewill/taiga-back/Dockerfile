FROM python:3.4  
EXPOSE 8000  
VOLUME /taiga/media  
VOLUME /taiga/static  
WORKDIR /taiga/taiga-back  
  
# Install dependencies  
RUN \  
apt-get update -qq && \  
apt-get install -y netcat gettext && \  
rm -rf /var/lib/apt/lists/*  
  
# Install taiga-back  
COPY requirements.txt ./requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Install plugins  
COPY plugins.txt ./plugins.txt  
RUN pip install --no-cache-dir -r plugins.txt  
  
# Copy source & config  
COPY . .  
RUN mv settings/local.py.docker ./settings/local.py  
  
RUN useradd -d /taiga taiga  
  
CMD ["./docker-entrypoint.sh"]  

