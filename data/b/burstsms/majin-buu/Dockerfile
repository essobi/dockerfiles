FROM ubuntu:14.04  
ARG BRANCH  
ARG GIT_SSH_PRIVATE  
  
MAINTAINER BurstSMS  
  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
zlib1g-dev \  
software-properties-common \  
wget \  
curl \  
sudo \  
git \  
python-pip \  
python-dev \  
python-software-properties \  
aptitude \  
python2.7 \  
nginx  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install nodejs  
RUN npm install -g pm2  
RUN npm install -g yarn  
RUN npm install -g mocha  
  
RUN mkdir -p /root/.ssh  
RUN echo "-----BEGIN RSA PRIVATE KEY-----" > /root/.ssh/id_rsa  
RUN echo $GIT_SSH_PRIVATE | sed "s/-----BEGIN RSA PRIVATE KEY----- //" | sed
"s/ -----END RSA PRIVATE KEY-----//" | tr ' ' '\n' >> /root/.ssh/id_rsa  
RUN echo "-----END RSA PRIVATE KEY-----" | tr -d '\n' >> /root/.ssh/id_rsa  
RUN chmod 400 /root/.ssh/id_rsa  
RUN touch /root/.ssh/known_hosts  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
RUN chmod 644 /root/.ssh/known_hosts  
RUN git clone -b $BRANCH git@bitbucket.org:shunz/majin-buu.git /opt/majin-buu  
WORKDIR /opt/majin-buu  
RUN rm -rf node_modules  
RUN yarn install  
  
COPY files/majin-buu-default.json /opt/  
ADD files/sites-available /opt/sites-available  
ADD files/ssl /opt/ssl  
  
COPY entrypoint.sh /  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

