FROM sylarchen/tushare-environment  
MAINTAINER Sylar Chen  
  
#ENV http_proxy 'http://web-proxy.atl.hp.com:8080'  
RUN apt-get update && \  
apt-get upgrade -y  
  
#build up python dependency  
RUN apt-get install -y libpq-dev python3-dev gcc  
#RUN pip --proxy http://web-proxy.atl.hp.com:8080 install psycopg2 threadpool  
RUN pip install psycopg2 threadpool  
  
#copy my source code to image  
RUN mkdir -p /DG  
ADD db_config.py /DG/  
ADD data_generator.py /DG/  
  
#set DB url  
ENV DB_URL 'postgresql://postgres:postgres@127.0.0.1/postgres'

