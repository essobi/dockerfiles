FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /dockerdjango  
WORKDIR /dockerdjango  
ADD requirements.txt /dockerdjango/  
RUN pip install -r requirements.txt  
ADD . /dockerdjango/

