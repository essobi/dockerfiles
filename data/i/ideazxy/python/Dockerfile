FROM python:3  
MAINTAINER Yudi <smartzxy@gmail.com>  
  
RUN pip install --trusted-host mirrors.aliyun.com -i
http://mirrors.aliyun.com/pypi/simple/ --no-cache-dir uwsgi  
  
RUN apt-get update && \  
apt-get install -y nginx pwgen supervisor curl unzip vim && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/log/supervisor  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install --trusted-host mirrors.aliyun.com -i
http://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt  
  
ONBUILD COPY . /usr/src/app  
  
CMD ["supervisord", "-n"]

