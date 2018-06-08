FROM node:7.10.0  
# The image already have a user with the guid and id 1000, called node...  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq sudo python-pip python-dev
&& \  
pip install awscli && \  
apt-get clean && \  
DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove python-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# adds the group  
RUN echo "node ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
## More setup  
RUN npm install -g @angular/cli@1.3.2 --no-spin --no-progress --loglevel warn  
  
# default user to run commands on the container, also all RUN commands from
this point are executed  
# with this user  
USER node  
  
## yarn setup  
RUN curl -o - -L https://yarnpkg.com/install.sh | bash -s -- --version 0.27.5  
  
RUN mkdir /home/node/app  
  
WORKDIR /home/node/app  

