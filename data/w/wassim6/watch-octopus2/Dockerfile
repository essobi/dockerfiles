FROM python:3.4  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y \  
python-pygraphviz  
  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/

