FROM python:3.6 as builder  
MAINTAINER Thomas LECLERCQ <contact@thomas.sh>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
# RUN python -m site  
# RUN ls /usr/local/lib/python3.6/site-packages/  
# FROM python:3-alpine3.6  
# COPY --from=builder /usr/local/lib/python3.6/site-packages/*
/usr/local/lib/python3.6/site-packages/  
# WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
EXPOSE 80  
CMD ["python", "run.py"]  

