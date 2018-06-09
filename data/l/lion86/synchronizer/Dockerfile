FROM ubuntu:latest  
  
MAINTAINER Leandro Silva <leandro.queiros.silva@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
freetds-dev \  
freetds-bin \  
unixodbc-dev \  
tdsodbc \  
python3-pip \  
python3-dev \  
nano \  
curl \  
tmux \  
htop \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip  
  
COPY docker /tmp/  
  
RUN pip3 install -r /tmp/requirements.txt  
  
RUN cat /tmp/odbc.ini >> /etc/odbc.ini  
RUN cat /tmp/freetds.conf >> /etc/freetds/freetds.conf  
RUN cat /tmp/odbcinst.ini >> /etc/odbcinst.ini  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
  
COPY . /home/sync  
WORKDIR /home/sync  
  
RUN cd /home/sync && npm install --save  
RUN npm install pm2 -g  
  
RUN rm -rf /home/sync/docker  

