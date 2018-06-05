FROM phusion/baseimage:0.9.13  
ENV HOME /root  
ENV CLOUDSTACK_REPO_URL https://github.com/apache/cloudstack.git  
ENV CLOUDSTACK_BRANCH 4.4-forward  
  
# Install required Packages  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections; \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections; \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections; \  
echo "mysql-server mysql-server/root_password password root" | debconf-set-
selections; \  
echo "mysql-server mysql-server/root_password_again password root" | debconf-
set-selections; \  
add-apt-repository -y ppa:webupd8team/java; \  
apt-get update; \  
apt-get install -y build-essential libreadline-gplv2-dev libncursesw5-dev
libssl-dev \  
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev git autoconf g++ \  
python2.7-dev python-setuptools python-pip \  
python-software-properties \  
oracle-java7-installer oracle-java7-set-default maven \  
mysql-server; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Reset MySQL Password  
RUN (/usr/bin/mysqld_safe &); sleep 3; mysqladmin -u root -proot password ''  
  
# Checkout CloudStack and Build CloudStack Simulator  
RUN cd $HOME; \  
git clone $CLOUDSTACK_REPO_URL; \  
cd $HOME/cloudstack; \  
git checkout $CLOUDSTACK_BRANCH; \  
mvn clean install -P developer -Dsimulator -DskipTests; \  
(/usr/bin/mysqld_safe &); \  
sleep 3; \  
mvn -Pdeveloper -pl developer -Ddeploydb; \  
mvn -Pdeveloper -pl developer -Ddeploydb-simulator; \  
mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION"  
  
# Change log level  
RUN sed -i -e 's/<param name="Threshold" value=".*"\/>/<param name="Threshold"
value="DEBUG"\/>/g' \  
$HOME/cloudstack/client/tomcatconf/log4j-cloud.xml.in  
  
# Install Marvin  
RUN cd $HOME/cloudstack; \  
mvn -Pdeveloper -pl :cloud-apidoc; \  
mvn -Pdeveloper -pl :cloud-marvin; \  
cd $HOME/cloudstack/tools/marvin; \  
python setup.py install  
  
# Install cloudmonkey  
RUN pip install cloudmonkey; \  
cloudmonkey init  
  
# Add runit scripts  
ADD etc/service/mysqld_safe/run /etc/service/mysqld_safe/run  
RUN chmod +x /etc/service/mysqld_safe/run  
  
ADD etc/service/cloudstack_simulator/run /etc/service/cloudstack_simulator/run  
RUN chmod +x /etc/service/cloudstack_simulator/run  
  
# Regenerate ssh key and remove unnecessary files  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init", "--enable-insecure-key"]  

