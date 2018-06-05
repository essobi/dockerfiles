FROM python:3.5  
EXPOSE 8000  
RUN apt-get update && apt-get install -y libpq-dev python3-dev gcc g++
libxslt-dev libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev
libwebp-dev tcl8.6-dev tk8.6-dev python-tk  
ENV LIBRARY_PATH=/lib:/usr/lib  
  
WORKDIR /app  
  
COPY requirements.txt /app  
RUN pip3 install -r requirements.txt  
COPY . /app  
VOLUME /app/staticfiles  
ENV DATABASE_URL postgres://postgresql:postgresql@db:5432/resa  
  
RUN chmod +x bash/run-prod.sh  
CMD /app/bash/run-prod.sh  

