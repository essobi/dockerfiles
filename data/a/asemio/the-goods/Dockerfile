FROM google/cloud-sdk AS base  
  
# set up terraform  
FROM google/cloud-sdk AS tf  
RUN apt-get -qqy update && apt-get install -qqy unzip  
RUN curl
https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip
-o terraform_0.11.7_linux_amd64.zip  
RUN unzip terraform_0.11.7_linux_amd64.zip -d terraform  
# install custom terraform kubernetes provider (so we can manage k8s
deployments in tf  
RUN curl -L https://github.com/sl1pm4t/terraform-provider-
kubernetes/releases/download/v1.1.0-custom/terraform-provider-
kubernetes_v1.1.0-custom_linux_amd64.zip -o terraform-provider-
kubernetes_v1.1.0-custom_linux_amd64.zip  
RUN unzip terraform-provider-kubernetes_v1.1.0-custom_linux_amd64.zip -d
tf-k8s  
  
# copy tf from intermediate layer  
FROM base AS final  
WORKDIR /usr/bin  
COPY \--from=tf /terraform .  
RUN mkdir ~/.terraform.d  
RUN mkdir ~/.terraform.d/plugins  
COPY \--from=tf /tf-k8s /root/.terraform.d/plugins  
  
# install node  
# replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get -y autoclean  
  
# nvm environment variables  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 8.11.2  
# install nvm  
# https://github.com/creationix/nvm#install-script  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash  
  
# install node and npm  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# confirm installation  
RUN node -v  
RUN npm -v  
  
WORKDIR /  
  

