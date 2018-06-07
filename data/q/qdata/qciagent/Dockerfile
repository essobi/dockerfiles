FROM ubuntu:16.04  
ENV CONSUL_TEMPLATE_VERSION=0.19.3  
#Setup  
RUN apt-get update  
RUN apt-get install -y curl unzip gpgv2 tar wget  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential software-properties-common locales
libbz2-dev zlib1g-dev && \  
locale-gen en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get install -y curl unzip jq php7.0 php7.0-cli php7.0-mysql php7.0-mcrypt
php7.0-bcmath php7.0-curl php7.0-xml php7.0-mbstring php7.0-gd php7.0-bz2
php7.0-zip git git-core git-extras lftp mongodb-org=3.0.12 mongodb-org-
server=3.0.12 mongodb-org-shell=3.0.12 mongodb-org-mongos=3.0.12 mongodb-org-
tools=3.0.12 && \  
echo "extension=mcrypt.so" >> /etc/php/7.0/cli/php.ini && \  
# Node version set 4.X to support Quantum Deployment  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
#Install Consul Template  
RUN ( curl https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o
/tmp/consul_template.zip && unzip /tmp/consul_template.zip && mv consul-
template /usr/bin && rm -rf /tmp/* )  
  
#Install Python  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev build-essential  
RUN apt-get install -y docker.io  
  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#Install front-end dependencies  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
RUN npm install -g gulp  
RUN npm install -g gulp-cli  
  
#Configure deploy by python  
RUN mkdir cmdtools  
COPY cmdtools/. cmdtools  
RUN cd cmdtools/deploytools && pip install -r requirements.txt  
  
#Configure deploy script  
ADD deploy.bash deploy.bash  
RUN chmod +x deploy.bash  
  
#Configure sass  
RUN wget -O sass.tar.gz https://github.com/sass/dart-
sass/releases/download/1.1.1/dart-sass-1.1.1-linux-x64.tar.gz  
RUN tar -xvzf sass.tar.gz  
ENV PATH="/dart-sass:${PATH}"  
CMD ["bash"]  

