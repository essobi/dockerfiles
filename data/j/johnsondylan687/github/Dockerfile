FROM python:2.7-slim  
  
WORKDIR /app  
  
ADD . /app  
  
RUN pip install -r requirments.txt  
  
RUN echo 'this is a update test' > /etc/testing  
  
EXPOSE 80:80  
ENV NAME World  
  
CMD ["python", "app.py"]  

