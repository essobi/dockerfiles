FROM fulbito/fulbito-python3  
  
ADD . usr/src/app  
  
WORKDIR usr/src/app  
  
RUN pip install uwsgi  
  
RUN pip install -r /usr/src/app/requirements.txt  
RUN pip install -r /usr/src/app/local-requirements.txt  
  
CMD /usr/local/bin/uwsgi --ini /usr/src/app/uwsgi.ini

