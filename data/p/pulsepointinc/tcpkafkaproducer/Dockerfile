FROM python:3.6-alpine  
  
CMD ["python", "/server.py"]  
  
RUN \  
pip install kafka-python && \  
rm -fr /root/.cache  
  
COPY ./server.py /server.py  

