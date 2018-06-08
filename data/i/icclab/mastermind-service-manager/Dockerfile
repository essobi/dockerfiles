FROM python:3.5-alpine  
  
WORKDIR /home/  
  
RUN apk add --update git nginx && \  
mkdir /run/nginx && \  
git clone https://github.com/icclab/MasterMind-ServiceManager.git && \  
cd MasterMind-ServiceManager && \  
pip3 install -r requirements.txt && \  
apk del git && \  
pip3 install gunicorn && \  
pip3 install .  
  
COPY run.sh /  
COPY nginx.conf /etc/nginx/  
  
WORKDIR /home/MasterMind-ServiceManager/  
  
ENTRYPOINT ["/run.sh"]  

