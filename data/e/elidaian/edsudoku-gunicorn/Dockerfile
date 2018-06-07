FROM python:2.7  
MAINTAINER Eli Daian "elidaian@gmail.com"  
# Install requirements  
ENV PYTHONUNBUFFERED 1  
ENV EDSUDOKU_CONF_FILE /var/edsudoku/edsudoku.cfg  
RUN mkdir /var/edsudoku  
ADD requirements.txt /var/edsudoku/requirements.txt  
RUN pip install -r /var/edsudoku/requirements.txt  
  
EXPOSE 8000  
ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:8000 edsudoku.wsgi:application  

