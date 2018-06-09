FROM codenvy/debian_jdk8_node  
  
RUN sudo apt-get update && \  
sudo apt-get install -y git git-svn tig screen ack-grep tofrodos vim && \  
sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# Install docker client + configure remote docker engine (so launching che
would work)  
#RUN sudo apt-get update && \  
# sudo apt-get install apt-transport-https ca-certificates && \  
# sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-
keys 58118E89F3A912897C070ADBF76221572C52609D && \  
# sudo -E bash -c "echo \"deb https://apt.dockerproject.org/repo ubuntu-trusty
main\" > /etc/apt/sources.list.d/docker.list" && \  
# sudo apt-get update && \  
# sudo apt-get install -y docker-engine && \  
# sudo apt-get clean && \  
# sudo rm -rf /var/lib/apt/lists/*  
#FLUX  
RUN sudo -E bash -c "echo \"deb http://www.rabbitmq.com/debian/ testing main\"
>> /etc/apt/sources.list" && \  
sudo wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc && \  
sudo apt-key add rabbitmq-signing-key-public.asc && \  
sudo apt-get update && \  
sudo apt-get install -y --allow-unauthenticated rabbitmq-server&& \  
sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3000  
ENV CODENVY_APP_PORT_3000_HTTP 3000  
WORKDIR /home/user/  
RUN wget https://github.com/eclipse/flux/archive/master.zip && \  
unzip master.zip && \  
rm master.zip  
  
WORKDIR /home/user/flux-master/node.server  
RUN sudo npm install --ignore-scripts  
  
#ENV FLUX_GITHUB_CLIENT_ID 6a6df7a17754389d04b8  
#ENV FLUX_GITHUB_CLIENT_SECRET 64141f3ddae3ad719cf35c43bf728286193df0f5  
ENV VCAP_APP_HOST 0.0.0.0  
WORKDIR /home/user/flux-master  
RUN wget
https://gist.githubusercontent.com/sunix/a9a1037e257da5d0a600/raw/3ff8a910f3400d19775bb562c89524518ac6f2d2/startup-
all-in-one.js.patch  
RUN patch -p1 < startup-all-in-one.js.patch  
# WORKDIR /home/user/flux-master/node.server  
#CMD sudo service rabbitmq-server start && npm start

