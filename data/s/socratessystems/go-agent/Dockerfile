FROM ubuntu:xenial  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common curl sudo  
  
RUN locale-gen en_US.UTF-8 && export LANG=en_US.UTF-8 && \  
add-apt-repository -y ppa:ondrej/php  
  
# yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get install -y apt-transport-https  
  
# node (which does an update, so might as well add it last to prevent multiple
updates)  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
  
RUN apt-get install -y openjdk-8-jre-headless git \  
php7.1-gmp php7.1-cli php7.1-mbstring php7.1-mcrypt php7.1-soap php7.1-xml
php7.1-json \  
php7.1-pdo-pgsql php7.1-pdo-mysql php7.1-mysqlnd php7.1-intl php7.1-curl
php7.1-gd \  
php7.1-ssh2 php7.1-dev php7.1-zip php7.1-gnupg nodejs yarn build-essential  
  
RUN npm install -g gulp bower webpack  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Add a user to run the go agent  
RUN adduser go --home /go  
  
# download the agent bootstrapper  
ADD https://github.com/ketan/gocd-golang-
bootstrapper/releases/download/0.9/go-bootstrapper-0.9.linux.amd64 /go/go-
agent  
RUN chmod 755 /go/go-agent  
  
RUN mkdir /go/.ssh  
  
# download tini  
ADD https://github.com/krallin/tini/releases/download/v0.10.0/tini /tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Run the bootstrapper as the `go` user  
USER go  
CMD /go/go-agent

