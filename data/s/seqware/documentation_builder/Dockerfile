# Build our documentation and push it to github  
FROM ubuntu:14.04  
MAINTAINER Denis Yuen <denis.yuen@oicr.on.ca>  
  
WORKDIR /root  
  
ADD config /root/.ssh/config  
ADD private_key.pem /root/.ssh/id_rsa  
RUN sudo apt-get update ; \  
sudo apt-get -y install ssh software-properties-common ;  
RUN sudo chown -R root /root/.ssh ;\  
sudo chmod -R 600 /root/.ssh/* ;\  
eval "$(ssh-agent -s)" ;\  
ssh-add ~/.ssh/id_rsa ;\  
sudo apt-add-repository -y ppa:rael-gc/rvm ;\  
sudo apt-get update ; \  
sudo apt-get -y install rvm git ruby1.9.3 ruby-rdiscount ruby-nokogiri ;  
  
# install java 8  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# install Maven 3.3.9  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
# enforce US locale, seems to better agree with gems  
USER root  
RUN sudo locale-gen en_US.UTF-8 ;\  
sudo dpkg-reconfigure locales ;\  
echo "export LANGUAGE=en_US.UTF-8" >> /etc/bash.bashrc ;\  
echo "export LANG=en_US.UTF-8" >> /etc/bash.bashrc ;\  
echo "export LC_ALL=en_US.UTF-8" >> /etc/bash.bashrc ;\  
echo "export LC_CTYPE=en_US.UTF-8" >> /etc/bash.bashrc ;\  
echo 'LANG="en_US.UTF-8"' | sudo tee /etc/default/locale ;\  
echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/default/locale ;\  
echo 'LC_CTYPE="en_US.UTF-8"' | sudo tee -a /etc/default/locale ;\  
echo 'LANG="en_US.UTF-8"' | sudo tee -a /etc/environment ;\  
echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/environment ;\  
echo 'LC_CTYPE="en_US.UTF-8"' | sudo tee -a /etc/environment  
  
RUN export LANGUAGE=en_US.UTF-8;\  
export LANG=en_US.UTF-8 ;\  
export LC_ALL=en_US.UTF-8 ;\  
export LC_CTYPE=en_US.UTF-8 ;\  
sudo gem install kramdown adsf mime-types compass haml coderay rubypants
builder rainpress yajl-ruby pygments.rb ;\  
sudo gem install nanoc -v 3.7.1 ;\  
sudo gem uninstall yajl-ruby --version 1.2.1  
  
RUN git config --global user.name "Seqware jenkins" ;\  
git config --global user.email seqware-jenkins@oicr.on.ca  
  
ADD settings.xml /root/.m2/settings.xml  
RUN git clone -b develop https://github.com/SeqWare/seqware.git  
WORKDIR /root/seqware  
# current gem version seems to fix the incompatibility  
RUN sudo gem install yajl-ruby  

