  
FROM hardbyte/python3  
MAINTAINER Brian Thorne <hardbyte@gmail.com>  
  
WORKDIR /app  
ONBUILD ADD . /app  
ONBUILD RUN virtualenv /env  
ONBUILD ADD requirements.txt /app/requirements.txt  
ONBUILD RUN /env/bin/pip install -r /app/requirements.txt  
  
EXPOSE 8080  
CMD []  
ENTRYPOINT ["/env/bin/python", "main.py"]  

