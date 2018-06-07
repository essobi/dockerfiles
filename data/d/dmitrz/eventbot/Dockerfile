FROM python:3.6-alpine3.7  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
ARG K8S_VERSION=v1.8.6  
RUN set -x && \  
wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/$K8S_VERSION/bin/linux/amd64/kubectl && \  
chmod +x /usr/local/bin/kubectl  
  
CMD [ "python", "bot.py" ]  

