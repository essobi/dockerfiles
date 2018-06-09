### STAGE 1: Build ###  
FROM centos:7 as builder  
  
ARG BUILD_ENV  
ARG SSHKEY  
  
# Install Dependencies  
RUN yum -y update \  
&& yum clean all \  
&& rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& yum -y install \  
bzip2 \  
gcc \  
git \  
htop \  
jq \  
nfs-utils \  
screen \  
tree \  
strace \  
wget \  
xorg-x11-server-Xvfb \  
make \  
which \  
java-devel \  
libdb-java-dev \  
python2.7-dev python-pip python-devel mysql-devel lzo lzo-devel PyQt4
PyQt4-webkit \  
libdb-devel \  
augeas  
  
RUN yum -y install centos-release-scl \  
&& yum -y install php55 php55-php php55-php-gd php55-php-mbstring php55-php-
mysqlnd php55-php-pdo \  
php-xmlwriter php-pdo_mysql  
  
# Enable ^^ installed files  
RUN echo "source scl_source enable php55 httpd24" >> ~/.bashrc  
  
# install ruby & compass  
RUN yum -y install gcc ruby-devel rubygems  
RUN gem install --no-rdoc --no-ri sass -v 3.4.22  
RUN gem install --no-rdoc --no-ri compass  
  
# Add N so we can install nodejs 9.2.1  
RUN curl -sL https://git.io/n-install | bash -s -- -y 9.2.1  
  
# Authorize SSH Host  
RUN mkdir -p /root/.ssh && \  
chmod 0700 /root/.ssh && \  
ssh-keyscan github.com > /root/.ssh/known_hosts  
  
# Add the key and set permissions  
RUN echo "$SSHKEY" > /root/.ssh/id_rsa && \  
chmod 600 /root/.ssh/id_rsa  
  
# Create a directory where our app will be placed  
RUN mkdir -p /usr/src/app  
  
# Change directory so that our commands run inside this new directory  
WORKDIR /usr/src/app  
  
# Get all the code needed to run the app  
COPY . /usr/src/app  
  
#ADD config/apache/aws.conf /etc/apache2/sites-enabled/000-default.conf  
ADD config/php/php.ini /opt/rh/php55/root/etc/php.ini  
  
# Install dependecies  
RUN source ~/.bashrc && ./build.sh $BUILD_ENV  
  
RUN ln -s /usr/src/app/web /opt/rh/httpd24/root/var/www/html/quicksight  
  
# cleanup  
RUN rm /root/.ssh/id_rsa  
  
EXPOSE 80  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD source ~/.bashrc && /opt/rh/httpd24/root/usr/sbin/apachectl -DFOREGROUND  

