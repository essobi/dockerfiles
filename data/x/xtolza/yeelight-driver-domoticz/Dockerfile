FROM python:alpine  
  
WORKDIR /app  
ADD * /app/  
RUN pip install -r requirements.txt  
ENV YEELIGHT_DEBUG=False  
  
EXPOSE 5000  
CMD ["python","/app/app.py"]  

