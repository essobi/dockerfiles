FROM python:3.6-slim  
  
ADD requirements.txt /tmp  
  
RUN pip install -r /tmp/requirements.txt  
  
COPY cmd.sh /  
COPY app.py /  
COPY /stockbot /stockbot  
  
VOLUME ["/persistence"]  
  
CMD ["/usr/bin/env", "bash", "/cmd.sh"]  

