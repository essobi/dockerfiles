FROM ubuntu:14.04  
MAINTAINER Nikolay Golub <nikolay.v.golub@gmail.com>  
  
WORKDIR /opt/kidstat  
COPY . /opt/kidstat  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y build-essential python3 python3-dev python3-setuptools
python3-pip && \  
pip3 install -r /opt/kidstat/kidstat/requirements/production.txt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5000  
CMD ["gunicorn", "--config", "deploy/gunicorn.conf.py", "--bind=0.0.0.0:5000",
"kidstat.wsgi:app"]  

