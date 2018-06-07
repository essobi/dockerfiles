FROM python:3.6-alpine  
  
CMD ["python", "/server.py"]  
  
RUN \  
pip install kafka-python==1.3.3 && \  
rm -fr /root/.cache  
  
COPY ./server.py /server.py  

