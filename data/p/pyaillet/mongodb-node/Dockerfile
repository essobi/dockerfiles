# Base image. You can pull from Docker Hub. Codenvy  
# provides a series of tested base images that include  
# Web Shell, installed utilities, and language support.  
# You can browse our images in Docker Hub or at  
# github.com/codenvy/dockerfiles. The shellinabox image  
# provides core Linux utilities and terminal access to runner.  
FROM codenvy/shellinabox  
  
ENV NODE_VERSION=0.12.9 \  
NODE_PATH=/usr/local/lib/node_modules  
  
# Codenvy uses this port to map IDE clients to the output of  
# your application executing within the Runner. Set these  
# values to the port of your application and Codenvy will  
# map this port to the output within the browser, CLI, and API.  
# You can set this value multiple times.  
# For example:  
# ENV CODENVY_APP_PORT_8080_HTTP 8080  
#  
# ENV CODENVY_APP_PORT_<port>_HTTP <port>  
# Codenvy uses this port to map IDE clients to the debugger  
# of your application within the Runner. Set these  
# values to the port of your debugger and Codenvy will  
# map this port to the debugger console in the browser.  
# You can set this value multiple times.  
# For example:  
# ENV CODENVY_APP_PORT_8000_DEBUG 8000  
#  
# ENV CODENVY_APP_PORT_<port>_DEBUG <port>  
# Set this value to the port of any terminals operating  
# within your runner. If you inherit a base image from  
# codenvy/shellinabox (or any of our images that inherit  
# from it, you do not need to set this value. We already  
# set it for you.  
# ENV CODENVY_WEB_SHELL_PORT <port>  
# Execute your custom commands here. You can add  
# as many RUN commands as you want. Combining  
# RUN commands into a single entry will cause your  
# environment to load faster. Also, building your image  
# with docker offline and uploading it to Docker Hub  
# as a pre-built base image will also cause it to load  
# Faster. This example installs python, curl, and the  
# Google SDK as an example.  
# RUN sudo apt-get update -y && \\\  
# sudo apt-get install --no-install-recommends -y -q curl build-essential
python3 python3-dev python-pip git python3-pip && \\\  
# sudo pip3 install -U pip && \\\  
# sudo pip3 install virtualenv && \\\  
# sudo mkdir /opt/googlesdk && \\\  
# wget -qO- \"https://dl.google.com/dl/cloudsdk/release/google-cloud-
sdk.tar.gz\" | sudo tar -zx -C /opt/googlesdk && \\\  
# sudo /bin/sh -c \"/opt/googlesdk/google-cloud-sdk/install.sh\" && \\\  
# sudo chmod +x /opt/googlesdk/google-cloud-sdk/bin/gcloud  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
&& \  
echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
sudo apt-get -y update && \  
sudo apt-get install -y mongodb-org && \  
sudo apt-get update && \  
sudo apt-get -y install build-essential libssl-dev libkrb5-dev gcc make ruby-
full rubygems curl && \  
sudo gem install sass compass && \  
sudo apt-get clean && \  
sudo apt-get -y autoremove && \  
sudo apt-get -y clean && \  
sudo rm -rf /var/lib/apt/lists/* && \  
set -ex && \  
for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done && \  
cd /home/user && curl --insecure -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
\  
&& curl --insecure -SLO
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep "node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& sudo tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local
\--strip-components=1 \  
&& sudo rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
ADD entrypoint.sh /entrypoint.sh  
RUN sudo chmod 777 /entrypoint.sh  
  
EXPOSE 3000 5000 9000  
RUN sudo npm install -g npm@latest  
RUN sudo npm install --unsafe-perm -g grunt grunt-cli  
  
# Include this as the CMD instruction in your Dockerfile if  
# you'd like the runner to stay alive after your commands  
# have finished executing. Keeping the runner alive is  
# necessary if you'd like to terminal into the image. If  
# your Dockerfile launches a server or daemon, like Tomcat,  
# you do not need to set this value as Docker will not  
# terminate until that process has finished.  
# CMD sleep 365d  

