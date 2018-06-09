FROM python:2.7.10  
MAINTAINER Kirsten Hunter (khunter@akamai.com)  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.4.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes -q curl
python-all wget vim python-pip php-pear php5 php5-mongo php5-dev ruby ruby-dev
perl5 npm  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes httpie
mongodb-org nodejs screen  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y --force-yes nodejs  
RUN mkdir -p /data/db  
ADD . /opt  
WORKDIR /opt  
RUN echo "export NODE_PATH=/opt/node_modules" >> /root/.bashrc  
RUN npm install  
ADD ./MOTD /opt/MOTD  
RUN echo "cat /opt/MOTD" >> /root/.bashrc  
RUN echo "PS1='Hapi.js API Course >> '" >> /root/.bashrc  
RUN echo "defshell -bash" > /root/.screenrc  
RUN cp /opt/mongod /etc/init.d/mongodb  
RUN chmod 777 /etc/init.d/mongodb  
ENTRYPOINT ["/bin/bash"]  

