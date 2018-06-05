FROM python:2.7-alpine  
MAINTAINER Artyom Aleksandrov  
  
RUN apk add --no-cache unzip  
#RUN git clone https://github.com/Flexget/Flexget.git /flexget && \  
ADD https://github.com/Flexget/Flexget/archive/develop.zip /flexget-dev.zip  
RUN mkdir -p /opt && \  
unzip /flexget-dev.zip -d /opt/ && \  
cd /opt/Flexget-develop && \  
pip install -e .  
ADD start.sh .  
VOLUME /root/.flexget  
WORKDIR /opt/Flexget-develop  
ENTRYPOINT ["/start.sh"]  
CMD ["--loglevel", "info", "daemon", "start", "--autoreload-config"]  
  

