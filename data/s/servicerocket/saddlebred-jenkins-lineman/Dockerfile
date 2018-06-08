FROM servicerocket/saddlebred-jenkinsslave  
MAINTAINER ServiceRocket Tools  
  
ENV NODE_VERSION 4  
RUN apt-get update -y && \  
apt-get install -y graphicsmagick imagemagick software-properties-common  
  
ENV NVM_DIR /nvm  
ENV PROFILE /etc/bash.bashrc  
RUN mkdir $NVM_DIR \  
&& chmod a+rw $NVM_DIR \  
&& mkdir p /npm \  
&& chmod a+rw /npm  
  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh |
sh \  
&& [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" \  
&& nvm install $NODE_VERSION \  
&& nvm use $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& npm install -g bower \  
&& npm install -g lineman  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 && \  
curl -L https://get.rvm.io | bash -s stable  
ENV PATH /usr/local/rvm/rubies/ruby-2.1.3/bin:/usr/local/rvm/bin:$PATH  
RUN rvm-shell && \  
rvm requirements && \  
rvm install 2.1.3 && \  
rvm use 2.1.3 --default  
  
# Global install required Ruby modules for activerecord  
RUN gem install sass -v 3.2.12  
  
# AWS CLI  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awscli  
  
ENV TERRAFORM_VERSION 0.6.8  
# Terraform CLI  
RUN wget -P /tmp
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \  
rm /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  

