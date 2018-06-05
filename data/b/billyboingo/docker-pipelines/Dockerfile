FROM markadams/chromium-xvfb  
  
MAINTAINER Bill Weiss <billyboingo@gmail.com>  
  
ENV NODE_SETUP_VER 8.x  
ENV TERRAFORM_VER 0.11.0  
RUN curl -sL https://deb.nodesource.com/setup_${NODE_SETUP_VER} | bash - \  
&& apt-get install -y nodejs openssh-client git wget zip unzip python-dev \  
&& rm -rf /var/lib/apt/lists \  
&& npm install -g yarn  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli  
  
RUN cd /usr/local && mkdir terraform \  
&& wget
https://releases.hashicorp.com/terraform/${TERRAFORM_VER}/terraform_${TERRAFORM_VER}_linux_amd64.zip
\  
&& unzip -n terraform_${TERRAFORM_VER}_linux_amd64.zip -d terraform \  
&& rm terraform_${TERRAFORM_VER}_linux_amd64.zip \  
&& ln -s /usr/local/terraform/terraform /usr/bin/terraform \  
&& terraform version

