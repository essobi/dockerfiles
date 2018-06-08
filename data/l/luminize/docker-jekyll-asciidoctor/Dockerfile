FROM ubuntu:15.10  
  
MAINTAINER Michael Haberler <haberlerm@gmail.com>  
  
RUN apt-get -y update && apt-get install -y \  
build-essential \  
curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y \  
asciinema \  
debconf \  
gcc \  
git \  
gnuplot \  
graphviz \  
imagemagick \  
libcurl3 \  
libjpeg-dev \  
libprotoc-dev \  
libprotobuf-dev \  
libyaml-dev \  
linkchecker \  
make \  
mscgen \  
nodejs \  
openjdk-8-jdk \  
protobuf-compiler \  
python-dev \  
python-gtk2 \  
python-pip \  
python-webcolors \  
python-numpy python-scipy python-matplotlib ipython ipython-notebook python-
pandas python-sympy python-nose \  
python-pil \  
python-protobuf \  
python-pygooglechart \  
python-setuptools \  
qt5-default \  
libqt5core5a \  
qt5-qmake \  
rsync \  
ruby-dev \  
w3c-linkchecker && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales && \  
pip install blockdiag actdiag seqdiag nwdiag && \  
pip install seaborn && \  
pip install prettyplotlib && \  
pip install shaape && \  
pip install python-frontmatter && \  
pip install blockdiagcontrib-octicons && \  
pip install blockdiagcontrib-cisco && \  
pip install blockdiagcontrib-class && \  
npm install -g mermaid && \  
npm install -g wavedrom-cli && \  
gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
curl -L https://get.rvm.io | bash -s stable && \  
mkdir /tmp/phantomjs && \  
curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs && \  
cd /tmp/phantomjs && \  
mv bin/phantomjs /usr/local/bin  
  
  
ENV LC_ALL=en_US.utf8 LANGUAGE=en_US.utf8  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN /usr/local/rvm/bin/rvm-shell && rvm requirements && rvm install 2.3.0 &&
rvm use 2.3.0 --default  
  
ENV PATH
/usr/local/rvm/rubies/ruby-2.3.0/bin:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
ADD ./Gemfile /root/  
  
RUN cd /root/ && \  
gem update --system && gem install bundler && bundle install && \  
git clone --depth=1 https://github.com/mhaberler/protoc-gen-doc.git && \  
cd protoc-gen-doc && \  
qmake && \  
make && \  
cp protoc-gen-doc /usr/local/bin && \  
cd /root/ && \  
git clone -b machinekit --single-branch
https://github.com/mhaberler/pygments.git && \  
cd pygments && \  
make mapfiles && \  
python setup.py install && \  
cd $(dirname $(gem which pygments.rb))/../vendor && \  
rm -rf pygments-main && \  
ln -s /root/pygments pygments-main && \  
cd $(dirname $(gem which pygments.rb))/.. && \  
ruby cache-lexers.rb  
  
# in case we use the image as a server  
# 35279 is for the LiveReload service  
EXPOSE 4000 80 443 35729  
  
WORKDIR /work  
  

