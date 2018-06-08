FROM tiangolo/uwsgi-nginx-flask:python3.6  
ENV FLASK_PORT 80  
COPY ./import_google_sheet /app  
COPY ./Pipfile /tmp  
COPY ./Pipfile.lock /tmp  
  
ENV SECRET_STORAGE_STRATEGY S3  
  
RUN ln -s /usr/local/bin/python /bin/python # Without this line, pipenv don't
work  
RUN pip3 install pipenv  
RUN cd /tmp && pipenv install --system

