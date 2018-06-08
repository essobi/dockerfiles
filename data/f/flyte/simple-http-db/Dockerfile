FROM python:3.6-alpine3.7  
WORKDIR /app  
COPY requirements.txt ./  
RUN pip install -r requirements.txt  
COPY server.py ./  
  
# Generally the host IP address  
ENV REDIS_HOST 172.17.0.1  
ENV HTTP_HOST 0.0.0.0  
ENV HTTP_PORT 5000  
EXPOSE 5000  
CMD ["python", "server.py"]  

