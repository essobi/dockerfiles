FROM ubuntu  
  
MAINTAINER Stephanie Baltus <stephanie.baltus@gmail.com>  
  
RUN apt-get update && apt-get install -y openssh-server  
  
RUN mkdir /var/run/sshd  
  
ADD sshd_config /etc/ssh/sshd_config  
  
CMD /usr/sbin/sshd -D  
  
RUN apt-get install -y vim  
  
RUN apt-get install -y postgresql-9.5  
  
RUN apt-get install -y libpq-dev python3-dev python-pip build-essential  
  
RUN yes | pip install --upgrade pip  
  
RUN yes | pip install --upgrade virtualenv  
  
RUN wget https://dl.influxdata.com/telegraf/releases/telegraf_1.1.2_amd64.deb  
  
RUN dpkg -i telegraf_1.1.2_amd64.deb  
  
RUN yes | pip install psycopg2  
  
RUN yes | pip install influxdb  
  
RUN yes | pip install Django==1.10.4  
  
RUN yes | pip install djangorestframework  
  
RUN yes | pip install django-filter  
  
RUN yes | pip install configparser  
  
RUN yes | pip install configobj  
  
RUN yes | pip install markdown  
  
RUN wget
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.3.1/elasticsearch-2.3.1.deb  
  
RUN dpkg -i elasticsearch-2.3.1.deb  
  
RUN systemctl enable elasticsearch.service  
  
RUN wget https://dl.influxdata.com/influxdb/releases/influxdb_1.1.1_amd64.deb  
  
RUN dpkg -i influxdb_1.1.1_amd64.deb  
  
RUN apt-get -y install git  
  
EXPOSE 2222  

