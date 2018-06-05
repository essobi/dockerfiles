FROM python:3  
MAINTAINER Learning map dev <admin@andela.com>  
  
ENV INSTALL_PATH /usr/src/learning_map_api  
ENV FLASK_APP="main.py"  
ENV FLASK_CONFIG 'development'  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
CMD gunicorn main:app --worker-class gevent --reload -b 0.0.0.0:8000 --access-
logfile -

