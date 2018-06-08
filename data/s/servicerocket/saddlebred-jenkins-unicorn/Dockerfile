FROM servicerocket/saddlebred-jenkinsslave  
MAINTAINER ServiceRocket Tools  
  
###  
# Jenkins slave to provide environment for Unicorn integration testing  
###  
ENV SCALA_VERSION 2.11.5  
# Maven + MySQL client + Ruby + XPdf dependencies  
RUN apt-get update -y && apt-get install -y \  
git-core \  
curl \  
zlib1g-dev \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt1-dev \  
libcurl4-openssl-dev \  
python-software-properties \  
libgdbm-dev \  
libncurses5-dev \  
automake \  
libtool \  
bison \  
libffi-dev \  
maven \  
libmysqlclient-dev \  
xpdf  
  
# Scala  
RUN apt-get remove scala-library scala && \  
wget http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.deb && \  
dpkg -i scala-$SCALA_VERSION.deb && \  
apt-get update && \  
apt-get install scala -y  
  
# OpenOffice 4.1.1 64bit  
RUN wget
http://downloads.sourceforge.net/project/openofficeorg.mirror/4.1.1/binaries/en-
US/Apache_OpenOffice_4.1.1_Linux_x86-64_install-deb_en-US.tar.gz && \  
tar -xzvf Apache_OpenOffice_4.1.1_Linux_x86-64_install-deb_en-US.tar.gz && \  
dpkg -i en-US/DEBS/*.deb && \  
apt-get update && \  
apt-get install openoffice -y  
  
# RVM and Ruby  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 && \  
curl -sSL https://get.rvm.io | bash -s stable --ruby  
ENV PATH /usr/local/rvm/rubies/default/bin:/usr/local/rvm/bin:$PATH  
RUN rvm-shell && \  
rvm requirements  
  
# Global install required Ruby modules for activerecord  
RUN /usr/local/rvm/rubies/default/bin/gem install bundler  
  
RUN echo "export PATH=$PATH" >> /root/.bashrc  
  
RUN update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
VOLUME ["/root/.m2/"]  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  

