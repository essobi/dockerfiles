FROM python:3.5  
# fist copy only requirements.txt, and run pip install  
# this enable better caching when building the image  
COPY requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
ADD . /app  
VOLUME ["/app/src", "app/var"]  
WORKDIR /app/src

