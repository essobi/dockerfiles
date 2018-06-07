FROM python:3.6-alpine  
WORKDIR /app  
ADD . /app  
RUN pip install --trusted-host pypi.python.org -r requirements.txt  
ENV USER user  
ENV PASSWORD password  
CMD ["python3", "app.py"]  

