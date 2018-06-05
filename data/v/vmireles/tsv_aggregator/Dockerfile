FROM python:3.6-alpine3.7  
ADD requirements.txt /requirements.txt  
#RUN pip install --no-cache-dir -r requirements.txt  
RUN mkdir /storage/  
ADD server.py /server/server.py  
CMD ["python", "/server/server.py"]  
  

