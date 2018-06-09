FROM python:3-alpine  
  
ADD requirements.txt /app/requirements.txt  
  
RUN pip install -r /app/requirements.txt  
  
ADD streaming.py /app/  
  
CMD [ "python", "./app/streaming.py" ]

