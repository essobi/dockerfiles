FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get -y install maven npm python-pip curl wget rebar git-core  
  
# install rvm and ruby 2.2.3 + bundler  
RUN bash -lc "(curl -sSL https://get.rvm.io | bash) && \  
source /usr/local/rvm/scripts/rvm && \  
rvm install 2.2.3 && \  
rvm use --default 2.2.3 && \  
gem install bundler"  
  
WORKDIR /usr/local  
  
# install rebar  
RUN bash -lc "git clone --depth 1 git://github.com/rebar/rebar.git && \  
cd rebar && \  
./bootstrap"  
  
# install gradle  
RUN wget http://services.gradle.org/distributions/gradle-2.4-bin.zip && \  
unzip gradle-2.4-bin.zip  
  
# install bower  
RUN npm install -g bower  
  
# install gvm and go 1.4.3, go 1.5 requires go 1.4 to bootstrap. Avoid the  
# headache and use 1.4.3  
RUN bash -lc "bash < <(curl -s -S -L \  
https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
&& \  
source $HOME/.gvm/scripts/gvm && \  
gvm install go1.4.3 && \  
gvm use 1.4.3 --default && \  
GOPATH=$HOME/go go get github.com/tools/godep"  
  
# TODO: remove from the install above  
RUN apt-get -y remove python-pip node  
  
RUN apt-get -y install nodejs nodejs-legacy  
  
RUN cd /tmp && \  
wget 'https://bootstrap.pypa.io/get-pip.py' && \  
python get-pip.py  
  
RUN echo '{"allowRoot": true}' > ~/.bowerrc  
  
ENV PATH=/usr/local/gradle-2.4/bin:/usr/local/rebar:/root/go/bin:$PATH  
  
# Fix the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US:en  
ENV LC_ALL=en_US.UTF-8  

