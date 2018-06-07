FROM python:3  
MAINTAINER mdruzkowski@digestoo.com  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
WORKDIR /usr/src/app/  
  
CMD PYTHONPATH=${PWD} twistd -n web --class=api.resource  
  
EXPOSE 5005  

