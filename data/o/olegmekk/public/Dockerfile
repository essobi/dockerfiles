FROM ubuntu  
  
  
  
# sudo install  
  
  
RUN apt-get update && \  
apt-get -y install sudo  
  
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
RUN useradd -m kevin && echo "kevin:kevin" | chpasswd && adduser kevin sudo  
  
CMD /bin/bash  
  
  
  
  
# Java install  
RUN apt-get update && \  
apt-get install -y wget software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
  
  
  
  
  
# Node  
  
RUN sed -e 's/^# deb /deb /g' /etc/apt/sources.list | grep "^deb " >
/etc/apt/sources.list.new && \  
mv /etc/apt/sources.list.new /etc/apt/sources.list && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \  
openssl \  
ca-certificates \  
rsyslog \  
rsyslog-relp \  
cron \  
curl \  
rsync \  
logrotate \  
gettext-base \  
wget \  
less \  
bash \  
bash-completion \  
tar \  
zip \  
unzip \  
git \  
emacs24-nox \  
jq figlet \  
build-essential \  
python \  
vim && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& apt-get update \  
&& sudo apt-get install -y nodejs  
# RUN wget -qO- https://deb.nodesource.com/setup_7.x | bash - && \  
# export DEBIAN_FRONTEND=noninteractive && \  
# apt-get update && \  
# apt-get install -y nodejs && \  
#apt-get clean && \  
#rm -rf /var/lib/apt/lists/*  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  

