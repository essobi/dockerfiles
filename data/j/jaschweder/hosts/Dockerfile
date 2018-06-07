FROM python:alpine  
  
COPY ./requirements.txt /requirements.txt  
  
RUN pip install -r /requirements.txt \  
&& rm -f /requirements.txt  
  
COPY ./hosts.py /hosts.py  
  
CMD ["python", "/hosts.py"]  

