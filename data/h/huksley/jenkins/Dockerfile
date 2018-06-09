FROM jenkins  
USER root  
RUN apt-get update && \  
apt-get install -y apparmor fetchmail procmail uudeview apt-transport-https
p7zip-full ca-certificates rsync yum-utils createrepo build-essential unzip
debmirror ubuntu-archive-keyring && \  
curl -sSL https://get.docker.com/ > /tmp/docker.sh && \  
bash /tmp/docker.sh && \  
usermod -aG docker jenkins && \  
curl -sL https://deb.nodesource.com/setup_6.x > /tmp/nodejs.sh && \  
bash /tmp/nodejs.sh && \  
apt-get install -y nodejs && \  
npm install bower -g && \  
groupadd -f rvm && \  
usermod -G rvm -a jenkins && \  
curl -sSL https://get.rvm.io > /tmp/ruby.sh && \  
bash /tmp/ruby.sh stable --ruby \--gems=jekyll && \  
rm -Rf /usr/local/rvm/src && \  
wget -O /tmp/apache-maven-3.3.9-bin.tar.gz http://apache-
mirror.rbc.ru/pub/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz && \  
cd /opt && \  
tar -xzvf /tmp/apache-maven-3.3.9-bin.tar.gz && \  
echo export PATH=/opt/apache-maven-3.3.9/bin:\$PATH >> /etc/profile.d/maven.sh
&& \  
apt-get install -y nuget && \  
curl -L https://services.gradle.org/distributions/gradle-2.14.1-bin.zip -o
gradle-2.14.1-bin.zip && \  
unzip gradle-2.14.1-bin.zip -d /opt && \  
echo 'export GRADLE_HOME=/opt/gradle-2.14.1' | tee -a $HOME/.bashrc && \  
echo 'export PATH=$PATH:$GRADLE_HOME/bin' | tee -a $HOME/.bashrc && \  
echo 'source /etc/profile.d/maven.sh' | tee -a $HOME/.bashrc && \  
echo 'source /etc/profile.d/nodejs.sh' | tee -a $HOME/.bashrc && \  
echo 'source /etc/profile.d/rvm.sh' | tee -a $HOME/.bashrc && \  
apt-get clean && \  
rm -Rf /var/lib/apt/lists/*  
USER jenkins  

