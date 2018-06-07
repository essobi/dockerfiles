FROM ubuntu:xenial  
  
RUN apt-get update &&\  
apt-get install -y wget curl git jq zip  
  
### BOSH CLI v2 ###  
RUN apt-get install -y build-essential zlibc zlib1g-dev libssl-dev
libreadline-dev  
RUN curl -vL https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-`curl -s
https://api.github.com/repos/cloudfoundry/bosh-cli/releases/latest | jq -r
.name | tr -d 'v'`-linux-amd64 -o /usr/local/bin/bosh &&\  
chmod +x /usr/local/bin/bosh  
  
### CF CLI ###  
RUN wget
"https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" -O -
| tar zxvf - cf &&\  
install -m 755 ./cf /usr/local/bin/ &&\  
rm ./cf  
  
### CF CLI plugins ###  
RUN cf install-plugin -f -r CF-Community update-cli  
  
### Ruby ###  
WORKDIR /root  
RUN git clone https://github.com/riywo/anyenv $HOME/.anyenv &&\  
echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> $HOME/.profile &&\  
echo 'eval "$(anyenv init -)"' >> $HOME/.profile &&\  
. $HOME/.profile &&\  
anyenv install rbenv &&\  
. $HOME/.profile &&\  
rbenv install 2.4.1 &&\  
rbenv global 2.4.1 &&\  
gem install bundler --no-ri --no-rdoc  
  
### UAA CLI ###  
RUN . $HOME/.profile &&\  
gem install cf-uaac --no-ri --no-rdoc  
  
### Concourse CLI ###  
RUN curl -vL https://github.com/concourse/concourse/releases/download/`curl -s
https://api.github.com/repos/concourse/concourse/releases/latest | jq -r
.tag_name`/fly_linux_amd64 -o /usr/local/bin/fly &&\  
chmod +x /usr/local/bin/fly  
  
### Minio CLI ###  
RUN curl -vL https://dl.minio.io/client/mc/release/linux-amd64/mc -o
/usr/local/bin/mc &&\  
chmod +x /usr/local/bin/mc  
  
### HashiCorp Vault ###  
RUN export VERSION=`curl -s https://api.github.com/repos/hashicorp/vault/tags
| jq -r '.[0] | ."name"' | sed 's/v//'` &&\  
curl -vL
https://releases.hashicorp.com/vault/${VERSION}/vault_${VERSION}_linux_amd64.zip
-o /tmp/vault.zip &&\  
cd /usr/local/bin &&\  
unzip /tmp/vault.zip &&\  
rm /tmp/vault.zip  
  
### HashiCorp Terraform ###  
RUN export VERSION=`curl -s
https://api.github.com/repos/hashicorp/terraform/releases/latest | jq -r
.tag_name | sed 's/v//'` &&\  
curl -vL
https://releases.hashicorp.com/terraform/${VERSION}/terraform_${VERSION}_linux_amd64.zip
-o /tmp/terraform.zip &&\  
cd /usr/local/bin &&\  
unzip /tmp/terraform.zip &&\  
rm /tmp/terraform.zip  
  
### additional tools ###  
RUN apt-get update &&\  
apt-get install -y vim tmux tree pwgen  
  
### gotty ###  
RUN curl -vL https://github.com/yudai/gotty/releases/download/`curl -s
https://api.github.com/repos/yudai/gotty/releases/latest | jq -r
.tag_name`/gotty_linux_amd64.tar.gz | tar zxvf - &&\  
cp ./gotty /usr/local/bin/ &&\  
rm ./gotty  
  
### usql ###  
RUN export VERSION=`curl -s
https://api.github.com/repos/xo/usql/releases/latest | jq -r .tag_name | sed
's/v//'` &&\  
curl -vL https://github.com/xo/usql/releases/download/`curl -s
https://api.github.com/repos/xo/usql/releases/latest | jq -r
.tag_name`/usql-${VERSION}-linux-amd64.tar.bz2 | tar jxvf - &&\  
cp ./usql /usr/local/bin/ &&\  
rm ./usql  
  
### Kubernetes CLI (kubectl) ###  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl &&\  
chmod +x ./kubectl &&\  
cp ./kubectl /usr/local/bin/ &&\  
rm ./kubectl  
  
### helm ###  
RUN curl -vL https://storage.googleapis.com/kubernetes-helm/helm-$(curl -s
https://api.github.com/repos/kubernetes/helm/releases/latest | jq -r
.tag_name)-linux-amd64.tar.gz | tar zxvf - linux-amd64/helm &&\  
cp ./linux-amd64/helm /usr/local/bin/ &&\  
rm -rf ./linux-amd64  
  
### CredHub CLI ###  
RUN export VERSION=$(curl -s https://api.github.com/repos/cloudfoundry-
incubator/credhub-cli/releases/latest | jq -r .tag_name) &&\  
curl -vL https://github.com/cloudfoundry-incubator/credhub-
cli/releases/download/$VERSION/credhub-linux-$VERSION.tgz | tar zxvf - &&\  
cp ./credhub /usr/local/bin/ &&\  
rm ./credhub  
  
### create workspace directory ###  
RUN mkdir /work  
WORKDIR /work  
  
ENTRYPOINT ["/bin/bash", "--login"]  

