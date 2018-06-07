FROM ubuntu:14.04.5  
MAINTAINER chinesedewey@gmail.com  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV NVM_DIR "/root/.nvm"  
ENV PATH "/root/.nvm/versions/node/v8.2.1/bin:${PATH}:/opt/cli_venv/bin"  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:deadsnakes/ppa \  
&& apt-get update \  
&& apt-get install -y \  
curl \  
git-all \  
python3.6 \  
python3.6-dev \  
python3.6-venv \  
wget \  
# These requirements are needed for running electron headless  
libgtk2.0-0 libgconf-2-4 libasound2 libxtst6 libxss1 libnss3 xvfb \  
&& apt-get clean  
  
RUN bash -c '\  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh |
bash; \  
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh"; \  
nvm install v8.2.1; \  
nvm use v8.2.1; \  
'  
  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O
/usr/local/bin/jq \  
&& chmod a+x /usr/local/bin/jq  
  
RUN python3.6 -m venv /opt/cli_venv \  
&& /opt/cli_venv/bin/pip install --upgrade awscli requests \  
&& rm -r /root/.cache/pip  

