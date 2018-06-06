FROM python:3.4.3  
#Add python app to the image  
RUN mkdir -p /app  
Add . /app  
WORKDIR /app  
  
CMD ["python", "setup.py", "install"]  
CMD ["python", "./crawler/main.py"]  

