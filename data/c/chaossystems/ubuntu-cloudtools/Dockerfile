ARG FROM_TAG=master  
FROM chaossystems/ubuntu-devtools:$FROM_TAG  
MAINTAINER Greg Orzell <chaos@chaossystems.io>  
  
# Cloud Tools  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && \  
apt-get install -y \  
google-cloud-sdk \  
python-dev \  
libpython-dev && \  
pip install --upgrade pip && \  
pip install setuptools wheel && \  
pip install aws-mfa awscli && \  
#npm install -g aws-sam-local && \  
curl -Lso /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-
cli-linux-amd64-latest && \  
chmod +x /usr/local/bin/ecs-cli && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/usr/bin/tmux"]  

