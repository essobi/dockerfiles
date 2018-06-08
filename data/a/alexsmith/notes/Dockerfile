FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip3 install -r requirements.txt  
RUN echo "deb http://packages.linuxmint.com debian import" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install firefox -y --force-yes  
ADD . /code/

