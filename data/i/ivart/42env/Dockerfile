FROM ivart/ubuntu-gc  
MAINTAINER Artem Ivanov <ivart@ivart.xyz>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
vim \  
zsh \  
krb5-kdc \  
wget \  
build-essential \  
python2.7-dev \  
python-pip \  
libkrb5-dev \  
libncurses-dev  
WORKDIR /root  
# Install OhMyZsh  
RUN curl https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -sSf | TERM=xterm bash  
# Set up kerberos  
RUN cp /etc/krb5.conf /etc/krb5.conf.bak && \  
echo "[libdefaults]\n\  
default_realm = 42.FR\n\  
forwardable = true\n\  
proxiable = true\n\  
dns_lookup_kdc = no\n\  
dns_lookup_realm = no\n\  
allow_weak_crypto = true\n" > /etc/krb5.conf && \  
echo "[realms]\n\  
42.FR = {\n\  
kdc = kdc1.42.fr\n\  
admin_server = kdc1.42.fr\n\  
default_domain = 42.fr\n\  
default_lifetime = 7d\n\  
ticket_lifetime = 7d\n\  
}\n" >> /etc/krb5.conf && \  
echo "[domain_realm]\n\  
.42.fr = 42.FR\n\  
42.fr = 42.FR\n" >> /etc/krb5.conf  
RUN mkdir -p ~/.ssh && \  
echo "# 42 vogsphere\nHost vogsphere.42.fr, vogsphere-exam.42.fr, vgs.42.fr,
vgse.42.fr\nStrictHostKeyChecking no" >> ~/.ssh/config  
# Install examshell  
RUN pip install virtualenv  
RUN git clone https://github.com/ivanovart/examshell42.git && \  
cd examshell42 && \  
./install.sh  
CMD ["zsh"]  

