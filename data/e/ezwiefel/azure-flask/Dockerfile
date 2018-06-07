FROM python:2.7  
  
USER root  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN apt-get update \  
&& apt-get install -y freetds-dev freetds-bin \  
&& pip install --no-cache-dir -r requirements.txt \  
&& echo America/Denver | tee /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata

