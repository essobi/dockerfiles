# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node,  
# plus dependencies for our build and some python tools we use for testing.  
# Note the plaintext password here; depending on your environment that may not
be advisable.  
# Based on evarga/jenkins-slave  
FROM makuk66/docker-oracle-java7  
MAINTAINER Martijn Koster "martijn.koster@lucidworks.com"  
# See http://phantomjs.org/download.html  
ENV PHANTOMJS_VERSION=2.1.1  
# Use the sha256 checksum for the linux-x86_64.tar.bz2  
ENV
PHANTOMJS_SHA256_CHECKSUM=86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f  
# Use our copy  
ENV PHANTOMJS_URL=https://s3.amazonaws.com/lucidworks-build-dependencies-
public/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2  
  
ENV
MAVEN_URL=https://archive.apache.org/dist/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.tar.gz  
  
ENV JENKINS_GID=7000  
ENV JENKINS_UID=7000  
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \  
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
&& \  
apt-get update  
  
RUN apt-get -y install build-essential libssl-dev libcurl4-openssl-dev
libexpat1-dev gettext libz-dev automake autoconf  
  
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \  
apt-get -y install ant openssh-server \  
build-essential libxml2-dev libxslt1-dev libxmlsec1-dev python-dev python-pip
\  
libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev \  
curl netcat-openbsd net-tools procps lsof rpm gnupg gnupg2 expect \  
libmysqlclient-dev libpq-dev libsvn-dev bzip2 libfreetype6 libfontconfig \  
unzip zip less vim smbclient && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd && \  
mkdir -p /var/run/sshd && \  
groupadd --gid $JENKINS_GID jenkins && \  
adduser --quiet --gecos "" \--disabled-password --uid $JENKINS_UID \--gid
$JENKINS_GID jenkins && \  
(echo "jenkins:jenkins" | chpasswd) && \  
mkdir -p /home/jenkins/.ssh && chown -R jenkins:jenkins /home/jenkins/.ssh  
RUN pip install virtualenv awscli beautifulsoup4  
RUN wget --no-verbose $PHANTOMJS_URL && \  
echo "$PHANTOMJS_SHA256_CHECKSUM phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2" > phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2.sha256 && \  
sha256sum -c phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2.sha256 && \  
rm phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2.sha256 && \  
tar xjC /opt < phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
rm phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
ln -s /opt/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs
/usr/local/bin/  
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \  
wget --no-verbose --output-document=- https://get.docker.com/ | sh && \  
usermod -aG docker jenkins  
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \  
apt-get -y install locales && \  
sed -i.bak -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen && \  
update-locale LC_ALL="en_US.UTF-8" && \  
export LANGUAGE=en_US:en && \  
export LANG=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
dpkg-reconfigure locales  
# Add maven, for #osdevs  
RUN mkdir -p /opt/apache-maven && \  
wget -nv --output-document=/opt/apache-maven.tgz $MAVEN_URL && \  
tar -C /opt/apache-maven --extract --file /opt/apache-maven.tgz --strip-
components=1 && \  
ln -s /opt/apache-maven/bin/mvn /usr/local/bin/mvn && \  
rm /opt/apache-maven.tgz  
# Add git  
RUN curl -L https://lucid-public-tools.s3.amazonaws.com/git/git-
bin-2.11.0.tar.gz -o /tmp/git.tar.gz && \  
tar -C / --extract --file /tmp/git.tar.gz && \  
/usr/bin/git --version && \  
rm /tmp/git.tar.gz  
ADD requirements.txt /tmp/requirements.txt  
ADD pyenv.sh /tmp/pyenv.sh  
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \  
bash -x /tmp/pyenv.sh  
  
ENV LANGUAGE en_US:en  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
EXPOSE 8764  

