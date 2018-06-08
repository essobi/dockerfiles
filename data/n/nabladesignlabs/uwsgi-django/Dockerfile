FROM python:3.4  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
COPY /myapp/requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
COPY /myapp /app  
RUN chown -R uwsgi /app  
COPY uwsgi.sh /uwsgi.sh  
RUN chmod +x /uwsgi.sh  
CMD ./uwsgi.sh  

