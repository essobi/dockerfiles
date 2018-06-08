# docker build -t telminov/fop-service .  
# docker push telminov/fop-service  
# docker run -ti --rm -p 8020:80 -v /var/docker/fop/conf:/conf telminov/fop-
service  
# docker run -d --restart always --name fop -p 8020:80 telminov/fop-service  
FROM ubuntu:16.04  
MAINTAINER telminov <telminov@soft-way.biz>  
  
RUN apt-get update && \  
apt-get install -y \  
vim \  
python3-pip \  
locales tzdata \  
default-jre  
  
RUN locale-gen ru_RU.UTF-8  
ENV LANG ru_RU.UTF-8  
ENV LANGUAGE ru_RU:ru  
ENV LC_ALL ru_RU.UTF-8  
COPY . /opt/fop-service  
WORKDIR /opt/fop-service  
  
RUN pip3 install -r requirements.txt  
RUN cp project/local_settings.sample.py project/local_settings.py  
  
EXPOSE 80  
VOLUME /conf/  
  
CMD test "$(ls /conf/local_settings.py)" || cp
project/local_settings.sample.py /conf/local_settings.py; \  
rm project/local_settings.py; ln -s /conf/local_settings.py
project/local_settings.py; \  
gunicorn project.wsgi --bind=0.0.0.0:80 --workers=5  

