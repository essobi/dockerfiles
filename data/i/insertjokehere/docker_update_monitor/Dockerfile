FROM python:3.6  
WORKDIR /src  
  
ADD requirements.txt /src/  
  
RUN pip install -r /src/requirements.txt  
  
ADD . /src/  
  
ENTRYPOINT ["python", "__init__.py"]  

