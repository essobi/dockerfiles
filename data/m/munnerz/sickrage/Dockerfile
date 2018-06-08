FROM python:2.7-alpine  
  
RUN apk add --no-cache \  
git  
  
ADD . /app  
  
WORKDIR "/app"  
  
EXPOSE 8081  
ENTRYPOINT ["python", "SickBeard.py"]  

