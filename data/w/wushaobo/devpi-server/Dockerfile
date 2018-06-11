FROM python:3.6  
COPY cn.list /etc/apt/sources.list  
RUN apt-get update && \  
apt-get install -y locales-all apache2-utils nginx && \  
apt-get clean  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN pip install \  
-i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com \  
devpi-server==4.3.2 \  
devpi-client==3.1.0 \  
devpi-web==3.2.1  
  
COPY run-server.sh /tmp/run-server.sh  
COPY nginx.conf /etc/nginx/nginx.conf  
  
CMD ["/tmp/run-server.sh"]  

