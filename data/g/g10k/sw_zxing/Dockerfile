# docker run -v $PWD:conf:/conf  
# docker run -it --name=mis_mm_zxing_2602
--volume="/var/docker/mis_mm_zxing_rotated/log_rotated:/var/log:rw"
--volume="/var/www/mis_mm_zxing_rotated/static:/static:rw"
--volume="/var/docker/mis_mm_zxing_rotated/data:/data:rw"
--volume="/var/docker/mis_mm_zxing_rotated/conf:/conf:rw" -p
0.0.0.0:8988:8080/tcp g10k/sw_zxing:rotated bash  
FROM ubuntu:14.04  
MAINTAINER Sergey Vlasov <g10k@soft-way.biz>  
ENV DEBIAN_FRONTEND=noninteractive  
  
EXPOSE 8080  
VOLUME /data/  
VOLUME /conf/  
VOLUME /static/  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
  
RUN add-apt-repository ppa:andrei-pozolotin/maven3  
  
RUN apt-get update  
RUN apt-get install maven3 git wget python-pip -y  
  
RUN mkdir /var/opt/zxing  
RUN git clone https://github.com/zxing/zxing.git /var/opt/zxing/  
  
WORKDIR /var/opt/zxing/  
RUN mvn install -Drat.ignoreErrors=true  
  
WORKDIR /var/opt/zxing/core  
RUN wget
http://central.maven.org/maven2/com/google/zxing/core/2.2/core-2.2.jar  
RUN mv core-2.2.jar core.jar  
RUN mvn install -Drat.ignoreErrors=true  
  
WORKDIR /var/opt/zxing/javase  
RUN wget
http://central.maven.org/maven2/com/google/zxing/javase/2.2/javase-2.2.jar  
RUN mv javase-2.2.jar javase.jar  
RUN mvn install -Drat.ignoreErrors=true  
  
WORKDIR /var/opt/zxing  
RUN git clone git://github.com/oostendo/python-zxing.git  
WORKDIR /var/opt/zxing/python-zxing  
RUN python setup.py install  
  
###################### Django application #################################  
# copy source  
COPY project/ /opt/sw_zxing  
WORKDIR /opt/sw_zxing  
  
RUN apt-get update  
RUN apt-get install python-dev libjpeg8-dev python-imaging supervisor -y  
RUN pip install -r requirements.txt  
RUN cp project/local_settings.sample.py project/local_settings.py  
RUN cp supervisor/prod.conf /etc/supervisor/conf.d/sw_zxing.conf  
  
# nginx  
RUN apt-get install nginx supervisor -y  
RUN mkdir /var/tmp/sw_zxing  
COPY nginx_gunicorn /etc/nginx/sites-enabled/  
  
CMD test "$(ls /conf/local_settings.py)" || cp
project/local_settings.sample.py /conf/local_settings.py; \  
rm project/local_settings.py; ln -s /conf/local_settings.py
project/local_settings.py; \  
rm -rf static; ln -s /static static; \  
python ./manage.py migrate; \  
python ./manage.py collectstatic --noinput; \  
/usr/bin/supervisord -c /etc/supervisor/supervisord.conf --nodaemon  
  

