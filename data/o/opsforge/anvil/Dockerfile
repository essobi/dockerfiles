# Dockerfile of opsforge.io DevUtils for PaaS use - Copyright (C) 2017 George
Svachulay - Apache 2.0 License  
FROM ubuntu:18.04  
ENV VAULTVER="0.9.6"  
ENV TFVER="0.11.6"  
ENV BOSHVER="3.0.1"  
MAINTAINER opsforge.io  
LABEL name="anvil"  
LABEL version="2.0.0"  
LABEL type="full"  
  
EXPOSE 5757  
VOLUME /root/repos  
  
# OS fixes and additions  
USER root  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install zip language-pack-en -y && \  
locale-gen en_GB.UTF-8 && \  
apt-get clean  
  
# Ubuntu package installs  
RUN apt-get -y install git zsh curl wget nano telnet dnsutils jq python-pip
python-dev libsqlite3-dev libffi-dev libssl-dev netcat sshpass inetutils-ping
vim git-crypt unzip pwgen groff && \  
apt-get clean  
  
# PIP package installs  
RUN pip install awscli && \  
pip install libsass && \  
pip install butterfly && \  
pip install aws-shell && \  
pip install boto3 && \  
pip install tile-generator  
  
# Install KOPS  
RUN cd /tmp && \  
curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s
https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name |
cut -d '"' -f 4)/kops-linux-amd64 && \  
chmod +x kops-linux-amd64 && \  
mv kops-linux-amd64 /usr/local/bin/kops  
  
# Install KubeCTL  
RUN cd /tmp && \  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl  
  
# Install VAULT  
RUN cd /tmp && \  
curl -LO
https://releases.hashicorp.com/vault/${VAULTVER}/vault_${VAULTVER}_linux_amd64.zip
&& \  
unzip vault_${VAULTVER}_linux_amd64.zip && \  
chmod +x vault && \  
mv vault /usr/local/bin/vault && \  
rm -rf /tmp/*  
  
# Install terraform  
RUN cd /tmp && \  
curl -LO
https://releases.hashicorp.com/terraform/${TFVER}/terraform_${TFVER}_linux_amd64.zip
&& \  
unzip terraform_${TFVER}_linux_amd64.zip && \  
chmod +x terraform && \  
mv terraform /usr/local/bin/terraform && \  
rm -rf /tmp/*  
  
# Install GO  
RUN apt-get update && \  
apt-get install -y golang && \  
apt-get clean  
  
# Install NodeJS  
RUN apt-get update && \  
apt-get install nodejs npm -y && \  
apt-get clean  
  
# Install Ruby stable  
RUN cd /tmp && \  
curl -sSL https://rvm.io/mpapis.asc | gpg --import - && \  
curl -sSL https://get.rvm.io | bash -s stable --ruby && \  
rm -rf /tmp/*  
  
# Install CF CLI using pivotal method  
RUN cd /tmp && \  
curl -L -o cf.deb
"https://cli.run.pivotal.io/stable?release=debian64&source=github" && \  
dpkg -i cf.deb && \  
rm -rf /tmp/*  
  
# Install OM  
RUN cd /tmp && \  
curl -LO https://github.com/pivotal-cf/om/releases/download/$(curl -s
https://github.com/pivotal-cf/om/releases/latest | sed 's/^.*tag\///' | sed
's/\".*$//')/om-linux && \  
chmod +x om-linux && \  
mv om-linux /usr/local/bin/om  
  
# Install BOSH cli  
RUN cd /tmp && \  
curl -LO https://s3.amazonaws.com/bosh-cli-artifacts/bosh-
cli-${BOSHVER}-linux-amd64 && \  
chmod +x bosh-cli-${BOSHVER}-linux-amd64 && \  
mv bosh-cli-${BOSHVER}-linux-amd64 /usr/local/bin/bosh  
  
# Install FLY CLI  
RUN cd /tmp && \  
curl -LO https://github.com/concourse/concourse/releases/download/$(curl -s
https://github.com/concourse/concourse/releases/latest | sed 's/^.*tag\///' |
sed 's/\".*$//')/fly_linux_amd64 && \  
chmod +x fly_linux_amd64 && \  
mv fly_linux_amd64 /usr/local/bin/fly  
  
# ZSH setup and terminal broadcasting  
RUN rm -rf ~/.git && \  
cd ~ && \  
rm -rf ~/.oh-my-zsh && \  
bash -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" && \  
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-
zsh/custom/themes/powerlevel9k  
COPY .zshrc /root/.zshrc  
RUN chmod 0755 /root/.zshrc  
  
# Set up butterfly SASS and powerlevel9k theme  
COPY style.sass /etc/butterfly/themes/powerlevel9k/style.sass  
RUN mkdir -p /etc/butterfly/themes/powerlevel9k && \  
chmod 0755 /etc/butterfly/themes/powerlevel9k/style.sass  
  
# Config entrypoint  
COPY entrypoint.sh /root/entrypoint.sh  
RUN chmod 0755 /root/entrypoint.sh  
  
SHELL ["/bin/zsh", "-c"]  
CMD ["/root/entrypoint.sh"]  

