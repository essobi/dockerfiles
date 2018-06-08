FROM supcik/texengine  
MAINTAINER Jacques Supcik <jacques@supcik.net>  
  
ADD fonts/* /usr/local/share/fonts/  
RUN fc-cache -fv  
  
RUN mkdir /app  
ADD doc_src /app/doc_src  
ADD groople /app/groople  
  
ADD *.py /app/  
ADD requirements.txt /app/  
ADD LICENSE.txt /app/  
  
WORKDIR /app  
RUN pip3 install -r requirements.txt  
  
ENV USER=root  
  
ENTRYPOINT ["python3", "./app.py"]

