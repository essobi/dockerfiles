FROM python:2.7-alpine  
RUN pip install web.py redis  
COPY addition.py /  
ENTRYPOINT ["python", "addition.py"]  
EXPOSE 8080  

