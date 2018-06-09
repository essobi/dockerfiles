FROM python:2.7-alpine  
  
RUN apk --update add --virtual build-dependencies python-dev build-base
libxml2-dev libxslt-dev libxslt py-lxml \  
&& pip install --upgrade pip  
WORKDIR /joinquant  
ADD requirements.txt /joinquant  
ADD main.py /joinquant  
RUN pip install -r requirements.txt  
ENTRYPOINT python main.py  

