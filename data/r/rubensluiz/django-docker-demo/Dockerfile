FROM python:3.6.4-alpine3.7  
EXPOSE 8000  
RUN apk add --no-cache curl  
ADD scripts/start.sh /  
RUN chmod +x /start.sh  
ADD requirements.txt /tmp  
RUN pip install --no-cache-dir -r /tmp/requirements.txt  
RUN rm /tmp/requirements.txt  
WORKDIR /app  
COPY src .  
  
HEALTHCHECK \--start-period=30s --interval=30s --timeout=3s \  
CMD curl -f http://localhost:8000/ || exit 1  
  
CMD [ "/start.sh" ]  

