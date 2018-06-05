FROM jenkins/jnlp-slave  
MAINTAINER Jason Gerry  
  
ENV TF_ALKS_PROVIDER_VERSION=0.9.11.1  
ENV TERRAGRUNT_VERSION=v0.14.10  
ENV PACKER_VERSION=1.2.3  
USER root  
  
### add to sudoers  
RUN usermod -aG sudo jenkins  
  
### dev tools  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get -y update  
RUN apt-get -y install apt-utils  
RUN apt-get -y upgrade  
RUN apt-get -y install build-essential readline-common libreadline-dev openssl
libssl-dev zlib1g-dev  
  
### jq  
RUN cd /usr/local/bin; curl -O
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64; mv jq-
linux64 jq; chmod 755 jq  
  
### alks  
RUN wget -q -O tfalks.tar.gz https://github.com/Cox-Automotive/terraform-
provider-alks/releases/download/${TF_ALKS_PROVIDER_VERSION}/terraform-
provider-alks-linux-amd64.tar.gz && \  
tar -zxvf tfalks.tar.gz -C /usr/bin/ && \  
chmod a+x /usr/bin/terraform-provider-alks  
  
### tfenv  
RUN git clone https://github.com/kamatama41/tfenv.git /opt/.tfenv  
RUN ln -s /opt/.tfenv/bin/tfenv /usr/local/bin/tfenv  
RUN ln -s /opt/.tfenv/bin/terraform /usr/local/bin/terraform  
RUN chown -R jenkins: /opt/.tfenv  
COPY .terraformrc /home/jenkins/.terraformrc  
RUN chown jenkins: /home/jenkins/.terraformrc  
  
### packer  
RUN wget
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip  
RUN unzip packer*  
RUN mv packer /usr/local/bin  
  
### terragrunt  
ADD https://github.com/gruntwork-
io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64
/bin/terragrunt  
RUN chmod +x /bin/terragrunt  
  
### rbenv  
RUN git clone https://github.com/rbenv/rbenv.git /home/jenkins/.rbenv  
RUN git clone https://github.com/rbenv/ruby-build.git
/home/jenkins/.rbenv/plugins/ruby-build  
RUN chown -R jenkins: /home/jenkins/.rbenv  
RUN ln -s /home/jenkins/.rbenv/bin/rbenv /usr/local/bin/rbenv  
  
### set default shell for jenkins user to bash  
RUN chsh -s /bin/bash jenkins  
  
USER jenkins  
  
RUN echo 'export PATH=~/.rbenv/shims:$PATH' >> ~/.bashrc  
RUN tfenv install 0.11.7  
RUN rbenv install 2.4.4  
RUN rbenv global 2.4.4  
  
ENTRYPOINT ["jenkins-slave"]  

