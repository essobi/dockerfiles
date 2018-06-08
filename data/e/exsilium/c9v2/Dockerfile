# Dockerfile  
FROM phusion/baseimage:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Bring in the latest and greatest  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Additional tools (python, g++, make are required for pty compilation)  
RUN apt-get install -y mc tig sudo python nginx g++-4.9 make  
  
RUN useradd -ms /bin/bash app  
USER app  
  
# Installing Node via NVM  
ENV NVM_DIR /home/app/.nvm  
ENV NODE_VERSION v6.11.5  
# Install nvm with node and npm  
RUN cd /home/app && curl
https://raw.githubusercontent.com/creationix/nvm/v0.33.5/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH  
  
RUN node --version  
RUN npm -v  
  
# Build instructions - Cloud9 Extras  
RUN mkdir /home/app/workspace && mkdir /home/app/cloud9-extra  
RUN git clone https://github.com/exsilium/cloud9.git /home/app/cloud9  
RUN git clone https://github.com/exsilium/cloud9-plugin-ungit.git
/home/app/cloud9-extra/cloud9-plugin-ungit  
RUN cd /home/app/cloud9-extra/cloud9-plugin-ungit && git checkout tags/v0.0.1
&& cd  
RUN ln -s /home/app/cloud9-extra/cloud9-plugin-ungit /home/app/cloud9/plugins-
client/ext.ungit  
  
# Build insturctions - Ungit  
RUN git clone https://github.com/exsilium/mungit.git /home/app/mungit  
RUN cd /home/app/mungit && git checkout tags/v1.2.0 && npm install -g grunt-
cli && npm install && grunt  
  
USER root  
  
RUN mkdir /etc/service/cloud9 && mkdir /etc/service/mungit && mkdir
/etc/service/nginx  
RUN printf "#!/bin/sh\nexec /usr/sbin/nginx -g 'daemon off;'" | tee
/etc/service/nginx/run  
RUN printf "#!/bin/sh\ncd /home/app/cloud9\nexec /sbin/setuser app
./node_modules/pm2/bin/pm2 start --no-daemon ecosystem.json" | tee
/etc/service/cloud9/run  
RUN printf "#!/bin/sh\ncd /home/app/mungit\nexec /sbin/setuser app ./bin/ungit
--port 8080 --urlBase \$C9_URLBASE --rootPath ungit --no-launchBrowser
--authentication --users.\$C9_USERNAME \$C9_PASSWORD" | tee
/etc/service/mungit/run  
RUN chmod 500 /etc/service/cloud9/run /etc/service/mungit/run
/etc/service/nginx/run  
  
# App setup  
RUN rm /etc/nginx/sites-enabled/default  
ADD cloud9.conf /etc/nginx/sites-enabled/cloud9.conf  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER app  
  
# c9v2 version setup  
ENV C9_CHECKOUT "tags/v2.1.6"  
RUN cd /home/app/cloud9 && git checkout $C9_CHECKOUT && export CXX=g++-4.9 &&
npm install && npm install pm2  
  
USER root  
  
# Environment variables used during runtime  
ENV C9_USERNAME test  
ENV C9_PASSWORD test  
ENV C9_WORKSPACE /home/app/workspace  
ENV C9_URLBASE http://my.domain.tld  
  
# Git environment variables, both must be set or git config alert will be
shown  
ENV GIT_AUTHOR_NAME "John Doe"  
ENV GIT_COMMITTER_NAME "John Doe"  
ENV GIT_AUTHOR_EMAIL "john@doe.na"  
ENV GIT_COMMITTER_EMAIL "john@doe.na"  
# Interfaces outside  
VOLUME ["/home/app/workspace"]  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  

