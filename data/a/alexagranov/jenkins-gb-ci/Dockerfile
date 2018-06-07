FROM mcpayment/ubuntu1404-java8  
  
# upgrade Ubuntu base  
RUN apt-get update && apt-get upgrade -y  
  
# basic packages  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
firefox \  
# chrome \  
libpq-dev \  
qt5-default \  
libqt5webkit5-dev \  
gstreamer1.0-plugins-base \  
gstreamer1.0-tools \  
gstreamer1.0-x \  
libsasl2-2 \  
libsasl2-modules \  
ntp \  
software-properties-common \  
xvfb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# kick up ntpd  
RUN ntpd  
  
# additional packages (for RVM, curl, etc.)  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
bison \  
curl \  
gawk \  
g++ \  
jq \  
libffi-dev \  
libgdbm-dev \  
libgmp-dev \  
libncurses5-dev \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libyaml-dev \  
make \  
pkg-config \  
postgresql-client \  
python-setuptools \  
python-pip \  
ruby-execjs \  
sqlite3 \  
unzip \  
zlib1g-dev  
  
# install geckodriver for selenium-webdriver  
RUN curl
https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
-O -L && \  
tar xvzf geckodriver-v0.20.1-linux64.tar.gz && \  
mv geckodriver /usr/local/bin  
  
# install chromedriver for Chrome  
# RUN export CHROMEDRIVER_VERSION=$(curl
http://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \  
# curl
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
-O -L && \  
# unzip chromedriver_linux64.zip && \  
# mv chromedriver /usr/local/bin  
# install s3cmd  
# RUN curl https://github.com/s3tools/s3cmd/archive/master.zip -O -L && \  
# unzip master.zip && \  
# cd s3cmd-master && \  
# python setup.py install  
RUN pip install s3cmd  
  
# install git-lfs for large files  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get install git-lfs -y  
  
# bump up file limits  
RUN ulimit -n 2048  
  
ENV HOME /home/jenkins  
# create jenkins user  
RUN useradd -d ${HOME} -m jenkins && \  
usermod -s /bin/bash jenkins && \  
usermod -a -G sudo jenkins  
# use EFS mount for Jenkins home  
ARG JENKINS_HOME=/var/lib/jenkins  
ENV JENKINS_HOME ${JENKINS_HOME}  
  
# copy over script that runs Jenkins...  
COPY run.sh ${HOME}  
RUN chown jenkins:jenkins ${HOME}/run.sh  
RUN chmod a+x ${HOME}/run.sh  
  
# copy over S3 fetch script...  
COPY try_fetch_backup.sh ${HOME}  
RUN chown jenkins:jenkins ${HOME}/try_fetch_backup.sh  
RUN chmod a+x ${HOME}/try_fetch_backup.sh  
  
# make backup dir  
ENV BACKUP_DIR=/data/backup  
RUN mkdir -p $BACKUP_DIR && chmod a+w $BACKUP_DIR  
  
# user-specific actions...  
USER jenkins  
ENV PATH=/usr/local/bin:$PATH  
  
# init git-lfs  
# RUN cd $HOME && git lfs install  
# set up vars to pull latest Jenkins backup file from S3  
ARG S3_BACKUP_BUCKET=backup.example.com  
ENV S3_BACKUP_BUCKET ${S3_BACKUP_BUCKET}  
ARG S3_BACKUP_PATH=jenkins  
ENV S3_BACKUP_PATH ${S3_BACKUP_PATH}  
  
# Install nvm with node and npm  
ENV NVM_DIR $HOME/.nvm  
ENV NODE_VERSION 7.10.1  
RUN cd && curl
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& ln -s $(which node) $(which node)js  
  
# install rvm  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB && \  
curl -sSL https://get.rvm.io | bash -s stable --autolibs=read-fail  
RUN /bin/bash -l -c "rvm install ruby-2.4.4"  
  
# write rvm init to .bashrc  
RUN echo '[[ -s "/home/jenkins/.rvm/scripts/rvm" ]] && source
"/home/jenkins/.rvm/scripts/rvm"' >> /home/jenkins/.bashrc  
  
# install latest Jenkins  
RUN cd $HOME && \  
curl http://mirrors.jenkins-ci.org/war/latest/jenkins.war -O -L  
  
VOLUME $JENKINS_HOME  
USER root  
EXPOSE 8080 5490  
CMD $HOME/run.sh $JENKINS_HOME  

