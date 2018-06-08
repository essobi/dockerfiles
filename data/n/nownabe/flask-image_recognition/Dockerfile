FROM nownabe/opencv3-python3  
MAINTAINER nownabe  
  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
  
ADD requirements.txt /usr/src/app/requirements.txt  
RUN pip install -r requirements.txt  
COPY . /usr/src/app  
  
CMD python app.py  

