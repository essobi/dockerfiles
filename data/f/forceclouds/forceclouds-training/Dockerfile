FROM python:3.6.3-alpine3.6  
COPY src /usr/src/  
RUN pip install -r /usr/src/requirements.txt  
EXPOSE 5000  
CMD ["python", "/usr/src/main.py"]

