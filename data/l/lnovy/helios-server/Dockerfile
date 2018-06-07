FROM debian:stretch  
  
EXPOSE 8000  
RUN apt-get update  
  
RUN apt-get install -y software-properties-common  
  
RUN apt-get upgrade -y && apt-get -y install python-virtualenv python-pip
unzip libpq-dev python-dev rabbitmq-server  
  
ADD https://github.com/pirati-cz/helios-server/archive/master.zip /helios/  
  
WORKDIR /helios/  
  
RUN unzip master.zip  
  
WORKDIR /helios/helios-server-master/  
  
RUN virtualenv venv  
  
RUN bash -c 'source venv/bin/activate; pip install -r requirements.txt'  
  
ADD docker-entrypoint.sh /  
  
RUN adduser --disabled-login --quiet --gecos Helios helios  
  
USER helios  
  
ENTRYPOINT /docker-entrypoint.sh  
  

