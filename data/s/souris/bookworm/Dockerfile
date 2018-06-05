FROM python:3.5  
MAINTAINER Tung Hoang  
  
  
ENV INSTALL_PATH /bookworm  
ENV URI 'http://bookworm_graph:ipbmX4LiLDcLHpM77RYX@hobby-
knhkoomjfhocgbkeonmkpenl.dbs.graphenedb.com:24789/db/data/'  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY . .  
  
WORKDIR "/bookworm"  
  
RUN pip install -r requirements.txt  
  
CMD gunicorn -b 0.0.0.0:3000 --access-logfile - "api.wsgi:app"  

