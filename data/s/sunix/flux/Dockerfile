FROM codenvy/jdk7  
RUN sudo -E bash -c "echo \"deb http://www.rabbitmq.com/debian/ testing main\"
>> /etc/apt/sources.list"  
RUN sudo wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc  
RUN sudo apt-key add rabbitmq-signing-key-public.asc  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y rabbitmq-server  
  
RUN sudo apt-get install -y nodejs-legacy npm  
  
EXPOSE 3000  
ENV CODENVY_APP_PORT_3000_HTTP 3000  
WORKDIR /home/user/  
RUN wget https://github.com/eclipse/flux/archive/master.zip  
RUN unzip master.zip  
  
WORKDIR /home/user/flux-master/node.server  
RUN sudo npm install  
  
#ENV FLUX_GITHUB_CLIENT_ID 6a6df7a17754389d04b8  
#ENV FLUX_GITHUB_CLIENT_SECRET 64141f3ddae3ad719cf35c43bf728286193df0f5  
ENV VCAP_APP_HOST 0.0.0.0  
WORKDIR /home/user/flux-master  
RUN wget
https://gist.githubusercontent.com/sunix/a9a1037e257da5d0a600/raw/3ff8a910f3400d19775bb562c89524518ac6f2d2/startup-
all-in-one.js.patch  
RUN patch -p1 < startup-all-in-one.js.patch  
WORKDIR /home/user/flux-master/node.server  
  
CMD sudo service rabbitmq-server start && npm start  

