FROM ubuntu  
MAINTAINER hpatel@channelit.biz  
USER root  
ENV\  
ES_VER=5.2.0  
RUN\  
apt-get update &&\  
apt-get install -y wget vim nodejs tar npm default-jdk sudo &&\  
apt-get update &&\  
wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-$ES_VER.tar.gz
&&\  
tar xzvf elasticsearch-$ES_VER.tar.gz &&\  
rm elasticsearch-$ES_VER.tar.gz &&\  
ln -s elasticsearch-$ES_VER es &&\  
touch start.sh &&\  
chmod 755 start.sh &&\  
echo "#!/bin/sh" >> start.sh &&\  
echo "su - elastic -c '/es/bin/elasticsearch'" >> start.sh  
RUN useradd -ms /bin/bash elastic &&\  
su - elastic &&\  
sudo chmod -R 777 /es  
EXPOSE 9200 9300  
ENTRYPOINT /start.sh  

