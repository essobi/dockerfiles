FROM python:3  
WORKDIR /code  
  
RUN git clone https://github.com/aaronduino/asciidots  
RUN pip3 install --no-cache-dir click  
  
ENTRYPOINT ["python", "asciidots/__main__.py"]  
  

