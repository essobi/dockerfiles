FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
WORKDIR /code  
  
RUN pip3 install --upgrade pip  
  
ADD requirements.txt /code  
RUN pip3 install -r requirements.txt  
  
ADD . /code  
  
CMD ["python3", "/code/main.py"]  

