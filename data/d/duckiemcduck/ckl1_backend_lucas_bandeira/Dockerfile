FROM python:3  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
RUN chmod +x /code/web-entrypoint.sh  
#ENV WAITFORIT_VERSION="v1.3.1"  
#RUN curl -o /usr/local/bin/waitforit -sSL
https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-
linux_amd64 && \  
#chmod +x /usr/local/bin/waitforit  
RUN chmod +x /code/wait-for-it.sh  
  
EXPOSE 8000  

