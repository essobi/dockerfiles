###### Docker image  
FROM qnib/d-node  
  
ENV RC_VERSION latest  
  
RUN groupadd rocketchat && \  
useradd -s /bin/false -d /opt/rocketchat/ -g rocketchat rocketchat  
# gpg: key 4FD08014: public key "Rocket.Chat Buildmaster
<buildmaster@rocket.chat>" imported RUN gpg --keyserver ha.pool.sks-
keyservers.net --recv-keys 0E163286C20D07B9787EBE9FD7F9D0414FD08104  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
0E163286C20D07B9787EBE9FD7F9D0414FD08104  
RUN mkdir -p /opt/rocketchat/ && \  
cd /opt/rocketchat/ && \  
curl -fSL "https://rocket.chat/releases/${RC_VERSION}/download" -o
rocket.chat.tgz && \  
curl -fSL "https://rocket.chat/releases/${RC_VERSION}/asc" -o
rocket.chat.tgz.asc && \  
gpg --verify rocket.chat.tgz.asc && \  
tar zxvf rocket.chat.tgz && \  
rm rocket.chat.tgz && \  
cd bundle/programs/server && \  
npm install  
ENV MONGO_URL=mongodb://mongodb:27017/meteor \  
PORT=3000 \  
ROOT_URL=http://0.0.0.0:3000  
ADD etc/supervisord.d/*.ini /etc/supervisord.d/  
ADD opt/qnib/rocketchat/bin/start.sh /opt/qnib/rocketchat/bin/  
ADD etc/consul.d/rocketchat.json /etc/consul.d/  
RUN apt-get install -y jq curl  

