FROM circleci/python:3.6.3-jessie-node-browsers  
  
ARG H=/home/circleci  
  
#
https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip  
RUN echo "alias ll='ls -alh'" >> ${H}/.bashrc && echo "set -o vi" >>
${H}/.bashrc  
  
RUN sudo npm install -g yarn@latest yuglify@latest  
  
RUN whoami; \  
cd /home/circleci; \  
sudo pip install -U awscli boto3; \  
pip --version; \  
aws --version;  
  
ADD build_container.bashrc /home/circleci/.bashrc  
  
RUN curl -sL https://sentry.io/get-cli/ | bash  
  
# Install jq  
RUN sudo wget -O "/usr/local/bin/jq"
"https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64"; \  
sudo chmod +x /usr/local/bin/jq  
  

