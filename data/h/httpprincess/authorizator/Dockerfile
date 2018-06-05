FROM debian:wheezy  
MAINTAINER jj  
RUN useradd autho  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install wget python python-pip -y && \  
apt-get clean autoclean && apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
RUN wget -O - --no-check-certificate
https://github.com/httpPrincess/authorizator/archive/master.tar.gz | tar zxf -
&& ln -s authorizator-master/ /app  
EXPOSE 5000  
WORKDIR /app/  
RUN pip install -r /app/requirements.txt && mkdir /app/myapp/data/ && echo
'{"service2":"simple"}' > /app/myapp/data/creds.json && /app/db_create.py &&
chown -R autho:autho /app/  
VOLUME /app/myapp/data/  
USER autho  
CMD /app/run.py  

