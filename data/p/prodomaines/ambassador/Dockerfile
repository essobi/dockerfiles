FROM python:3.5-slim  
  
RUN apt-get update && apt-get install -y socat && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["python", "/main.py"]  
  
ADD requirements.txt /requirements.txt  
ADD main.py /main.py  
RUN pip install -r /requirements.txt  

