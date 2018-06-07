FROM python:3.6  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
  
COPY ./requirements.txt /config/  
COPY bin/cmd.sh /  
  
RUN pip install -r /config/requirements.txt  
  
WORKDIR /app  
  
USER uwsgi  
  
CMD ["/cmd.sh"]  

