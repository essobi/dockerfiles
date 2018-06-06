# Arch_Celery  
FROM openmarble/arch-vips:latest  
MAINTAINER Andreas Trawöger <atrawog@openmarble.org>  
  
RUN rm /usr/sbin/python && \  
rm /usr/sbin/pip && \  
pacman -Syuq --noconfirm --needed python python-setuptools python-pip && \  
pacman -Sc --noconfirm  
  
RUN pip install --upgrade redis && \  
pip install --upgrade celery && \  
pip install --upgrade flower && \  
mkdir -p /code /conf /data /secret  
  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
ENV REDIS_DATABASE 0  
VOLUME [" /code","/conf","/data","/secret"]  
  
WORKDIR /code  
  
CMD /usr/sbin/celery -A tasks worker -l INFO
--broker=redis://$REDIS_HOST:$REDIS_PORT/$REDIS_DATABASE \--workdir=/code

