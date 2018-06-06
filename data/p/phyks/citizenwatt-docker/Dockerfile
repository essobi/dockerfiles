FROM ubuntu:14.04  
MAINTAINER Phyks <phyks@phyks.me>  
  
# Set LANG  
ENV LANG C.UTF-8  
# Install packages  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y postgresql postgresql-server-dev-all redis-server
python3 python3-pip build-essential python3-dev git  
RUN pip3 install requests sqlalchemy pycrypto numpy cherrypy psycopg2 redis  
  
# Configure the system  
ADD init.sh /tmp/init.sh  
RUN chmod 775 /tmp/init.sh  
RUN /tmp/init.sh  
RUN rm /tmp/init.sh  
  
RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/"
/etc/postgresql/9.3/main/postgresql.conf  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
# Get CitizenWatt  
RUN git clone https://github.com/CitoyensCapteurs/CitizenWatt-Base
/opt/citizenwatt  
ADD test_process.py /opt/citizenwatt/test_process.py  
RUN chmod 775 /opt/citizenwatt/test_process.py  
# Init CitizenWatt config  
RUN cd /opt/citizenwatt && echo "import libcitizenwatt.config as config; c =
config.Config()" | python3  
  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
  
ENTRYPOINT ["/bin/bash", "-e", "/start.sh"]  
  
EXPOSE 8080  

