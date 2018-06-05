FROM python:2.7  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y uwsgi uwsgi-plugin-python python-
psycopg2 libpq-dev python-dev binutils libproj-dev gdal-bin libxml2-dev
libxslt1-dev && rm -rf /var/lib/apt/lists/*  
EXPOSE 8000  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
CMD ["./run.sh"]

