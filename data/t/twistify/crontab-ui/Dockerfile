# BUILD: sudo docker build -t crontab-ui .  
# RUN: sudo docker run -it -d -p 8000:8000 --name crontab-ui twistify/crontab-
ui  
FROM alpine:3.5  
LABEL maintainer "@twistify"  
LABEL description "Crontab-UI on Alpine Linux"  
  
RUN apk --no-cache add \  
nodejs \  
ca-certificates \  
wget \  
curl  
  
RUN update-ca-certificates  
  
RUN npm install -g crontab-ui  
  
# copy and prepare our startup script  
COPY startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
ENV HOST 0.0.0.0  
ENV PORT 8000  
EXPOSE $PORT  
ENTRYPOINT ["./startup.sh"]  

