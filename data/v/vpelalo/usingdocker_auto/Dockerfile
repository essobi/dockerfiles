FROM python:3.4  
COPY requirements.txt /tmp/  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install -r /tmp/requirements.txt  
WORKDIR /app  
COPY app /app  
COPY cmd.sh /  
  
EXPOSE 9090 9191  
USER uwsgi  
  
CMD ["/cmd.sh"]  

