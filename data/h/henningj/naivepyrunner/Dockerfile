from python:3  
RUN pip install wheel pip -U --no-cache-dir  
  
WORKDIR /npr  
COPY ./ /npr  
RUN pip install .  
  
WORKDIR /app  
RUN rm -rf /npr  

