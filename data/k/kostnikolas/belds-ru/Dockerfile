FROM ubuntu:latest  
MAINTAINER kostnikolas <kostnikolas@yandex.ru>  
RUN apt-get update \  
&& apt-get install -y python3-pip python3-dev \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip  
RUN apt-get install libmysqlclient-dev -y  
RUN apt-get install git -y  
RUN pip install mysqlclient  
ENV LIBRARY_PATH=/lib:/usr/lib  
ADD . /usr/src/app  
WORKDIR /usr/src/app  
RUN mkdir logs  
RUN mv docker_local_settings_template.py local_settings.py  
RUN pip install -r requirements.txt  
RUN chmod +x docker-entrypoint.sh  
EXPOSE 8000  
ENTRYPOINT ["./docker-entrypoint.sh"]

