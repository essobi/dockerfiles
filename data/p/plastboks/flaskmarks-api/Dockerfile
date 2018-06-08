FROM ubuntu:14.04  
MAINTAINER Alexander Skjolden alex@plastboks.net  
  
RUN apt-get update  
#RUN apt-get upgrade  
RUN apt-get -y install build-essential  
RUN apt-get -y install git  
RUN apt-get -y install python-virtualenv  
RUN apt-get -y install python2.7-dev  
  
VOLUME /flaskmarks/shared  
  
RUN mkdir -p /opt/virtualenvs  
WORKDIR /opt/virtualenvs  
RUN git clone https://github.com/plastboks/Flaskmarks-API.git app  
WORKDIR /opt/virtualenvs/app  
RUN pip install -r requirements.txt  
RUN cp config/default.py.example config/default.py  
RUN cp config/development.py.example config/docker.py  
RUN sed -i s/REPLACE_ME/$(python -c "import uuid;print uuid.uuid4()")/g
config/default.py  
ENV APP_CONFIG_FILE /opt/virtualenvs/app/config/docker.py  
RUN python run.py db init  
RUN python run.py db migrate  
RUN python run.py db upgrade  
  
USER daemon  
EXPOSE 5000  
ENTRYPOINT ["python"]  
  

