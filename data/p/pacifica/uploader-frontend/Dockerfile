FROM python:2.7-jessie  
MAINTAINER david.brown@pnnl.gov  
  
RUN apt-get update && apt-get -y install expect && apt-get clean all  
ENV PYTHONPATH /src  
ADD ./requirements.txt /src/requirements.txt  
WORKDIR /src  
RUN pip install --no-cache-dir -r requirements.txt  
ADD . /src  
RUN python manage.py migrate  
  
EXPOSE 8000  
ENTRYPOINT ["gunicorn", "UploadServer.wsgi:application", "-w", "2", "-b",
":8000", "--log-level", "debug", "--proxy-allow-from", "*", "--reload" ]  

