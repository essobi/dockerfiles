FROM python:2.7  
RUN apt-get update -y  
RUN apt-get -y install binutils libproj-dev gdal-bin python-libvoikko voikko-
fi  
COPY requirements.txt manage.py /usr/src/app/  
COPY decisions /usr/src/app/decisions/  
COPY vendor /usr/src/app/vendor/  
WORKDIR /usr/src/app/  
RUN pip install -r requirements.txt --src /usr/local/src  
CMD /usr/local/bin/gunicorn decisions.wsgi:application -w 2 -b :8000

