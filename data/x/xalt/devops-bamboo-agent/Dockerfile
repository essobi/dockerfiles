FROM java:8u40-b22-jre  
MAINTAINER Philipp Goellner <philipp.goellner@xaltbc.de>  
  
ENV TIME_ZONE false  
  
ENV BAMBOO_AGENT_HOME /var/atlassian/bamboo-agent  
ENV BAMBOO_AGENT_TIMEOUT 90  
ENV BAMBOO_SERVER false  
ENV ANSIBLE_HOST_KEY_CHECKING false  
  
RUN apt-get update --quiet \  
&& apt-get install --quiet -y ansible \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
jq \  
python-pip \  
python3-pip \  
software-properties-common \  
tzdata \  
wget \  
&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \  
  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian jessie stable" \  
&& apt-get update --quiet \  
&& apt-get install --quiet -y docker-ce=17.09.1~ce-0~debian \  
&& pip install --upgrade pip \  
awscli \  
&& pip3 install requests \  
&& curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& apt-get install -y nodejs \  
&& apt-get clean \  
&& curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose \  
&& chmod 0755 /usr/local/bin/docker-compose \  
&& curl -L
https://github.com/gohugoio/hugo/releases/download/v0.36.1/hugo_0.36.1_Linux-64bit.tar.gz
| tar xvz -C /usr/local/bin/ hugo \  
&& chmod 0755 /usr/local/bin/hugo \  
&& pip3 install google-api-python-client \  
&& pip3 install gspread \  
&& pip3 install mws  
  
ADD configure-and-start-root.sh /  
  
VOLUME ["${BAMBOO_AGENT_HOME}"]  
  
VOLUME ["/root/.aws"]  
  
# It is also recommended to link private and public ssh-key for ansible  
# Here the paths to those files:  
#  
# /root/.ssh/id_rsa  
# /root/.ssh/id_rsa.pub  
# Run Atlassian Bamboo Agent as foreground process by default.  
ENTRYPOINT ["/configure-and-start-root.sh"]  

