FROM 'ubuntu:trusty'  
RUN apt-get update -qq && apt-get install -qqy curl software-properties-common
apt-transport-https  
RUN sh -c 'curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -'  
RUN sh -c 'curl
https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
> /etc/apt/sources.list.d/dart_stable.list'  
RUN mkdir $HOME/.virtuanenvs && echo "export WORKON_HOME=$HOME/.virtualenvs"
>> $HOME/.bashrc  
RUN add-apt-repository ppa:gophers/archive  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-get update -qq && apt-get -qqy install \  
git \  
golang-1.9-go \  
python3-pip \  
python-dev \  
build-essential \  
virtualenvwrapper \  
openjdk-8-jdk \  
maven \  
dart \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt-get -y clean autoclean autoremove  
  
ENV PATH="/usr/lib/go-1.9/bin:/root/go/bin:${PATH}"  
RUN go get github.com/tools/godep  
RUN pip install -U setuptools virtualenv virtualenvwrapper  
RUN echo "source /etc/bash_completion.d/virtualenvwrapper" >> $HOME/.bashrc

