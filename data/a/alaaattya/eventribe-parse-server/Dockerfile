FROM ubuntu:14.04  
MAINTAINER Alaa Attya a.attya@entlaqa.com  
  
RUN apt-get update  
  
# install vim  
RUN apt-get install -y vim  
  
# install curl  
RUN apt-get install -y curl  
  
# install git  
RUN apt-get install -y git-core  
  
# install nodejs  
RUN sudo apt-get update && \  
sudo apt-get install -y build-essential libssl-dev libmysqlclient-dev && \  
sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#ENV NODE_VERSION 5.10.1  
#RUN curl --location https://raw.github.com/creationix/nvm/master/install.sh |
sh && \  
# sudo /bin/bash -c "echo \"[[ -s \$HOME/.nvm/nvm.sh ]] && .
\$HOME/.nvm/nvm.sh\" >> /etc/profile.d/npm.sh" && \  
# echo "[[ -s $HOME/.nvm/nvm.sh ]] && . $HOME/.nvm/nvm.sh" >> $HOME/.bashrc  
#RUN . ~/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm alias default
$NODE_VERSION && nvm use default  
#ENV PATH $HOME/.nvm/bin:$PATH  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 5.2.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
# install mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
RUN apt-get update  
RUN apt-get install -y mongodb-org  
  
# fix mongo internationalisation issue  
RUN export LC_ALL=C  
  
RUN mkdir -p /data/db  
RUN mkdir -p /logs  
  
# Backup original MongoDB config  
RUN mv /etc/mongod.conf /etc/mongod.orig.conf  
  
# Copy in custom MongoDB config  
ADD ./mongod.conf /etc/mongod.conf  
  
# allow mongo ports  
EXPOSE 27017 28017  
RUN mkdir -p /scripts  
  
# create script output folder  
RUN mkdir -p /scripts/output  
  
# add db credentials as enviroment variables  
ENV MONGO_DB_NAME entlaqa  
ENV MONGO_DB_USER entlaqa2  
ENV MONGO_DB_PASSWORD admin123m  
  
ENV HOST_IP 192.168.99.100  
VOLUME /data/db  
  
ENV AUTH yes  
ENV STORAGE_ENGINE wiredTiger  
ENV JOURNALING yes  
  
  
# run the app shell configs  
ADD run.sh /scripts/run.sh  
ADD set_mongodb_cred.sh /scripts/set_mongodb_cred.sh  
ADD generate_parse_dashboard_config.sh
/scripts/generate_parse_dashboard_config.sh  
  
# install npm  
RUN apt-get install -y npm  
  
# this bitch took me 4 hours to solve the permission denied issue  
RUN chmod a+x /scripts/run.sh  
RUN chmod a+x /scripts/set_mongodb_cred.sh  
RUN chmod a+x /scripts/generate_parse_dashboard_config.sh  
  
#CMD ["/scripts/generate_parse_dashboard_config.sh"]  
CMD ["/scripts/run.sh"]  
  
# setup parse server  
ADD /app /app  
WORKDIR /app  
RUN npm install  
  
# setup parse app credentials  
ENV APP_ID 123  
ENV MASTER_KEY 123  
ENV DATABASE_URI
mongodb://$MONGO_DB_USER:$MONGO_DB_PASSWORD@$HOST_IP:27017/$MONGO_DB_NAME  
ENV APP_NAME Eventribe  
  
EXPOSE 1337  
CMD [ "npm", "start" ]  
  
# Parse dashboard  
ENV PARSE_DASHBOARD_ALLOW_INSECURE_HTTP 1  
ENV SERVER_URL http://$HOST_IP:1337/parse  
ENV PARSE_AUTH_USERNAME admin  
ENV PARSE_AUTH_PASSWORD admin@123  
RUN npm install -g parse-dashboard  
  
EXPOSE 4040  
RUN parse-dashboard &

