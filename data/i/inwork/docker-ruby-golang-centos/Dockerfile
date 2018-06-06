FROM centos:7  
MAINTAINER "http://www.inwork.ch"  
# change here the versions  
# ruby version can be found here https://github.com/rbenv/ruby-
build/tree/master/share/ruby-build  
ENV RUBY_VERSION 2.0.0-p648  
ENV GOLANG_VERSION 1.6.2  
ENV GLIDE_VERSION 0.11.0  
ENV GOPATH /go  
  
# find URL and SHA1 on https://golang.org/dl/  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
e40c36ae71756198478624ed1bb4ce17597b3c19d243f3f0899bb5740d56212a  
  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/v$GLIDE_VERSION/glide-v$GLIDE_VERSION-
linux-amd64.tar.gz  
  
# install general pre-requisites  
RUN yum install -y epel-release  
RUN yum install -y tar git git-core sqlite sqlite-devel make gcc gcc-c++ patch
ruby-devel zlib zlib-devel postgresql-devel \  
cmake openssh-client libxml2-devel libxslt-devel nodejs npm curl rpm-build
readline readline-devel \  
libyaml-devel libffi-devel openssl-devel bzip2 autoconf automake libtool bison
wget rubygems redis  
  
# install rbenv  
RUN git clone git://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN echo 'export PATH="/root/.rbenv/bin:$PATH"' >> /root/.bash_profile  
  
RUN echo 'eval "$(rbenv init -)"' >> /root/.bash_profile  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN git clone git://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN echo 'export PATH="/root/.rbenv/plugins/ruby-build/bin:$PATH"' >>
/root/.bash_profile  
  
ENV PATH /root/.rbenv/bin:$PATH  
RUN exec $SHELL  
  
# install ruby  
RUN rbenv install -v $RUBY_VERSION  
RUN rbenv global $RUBY_VERSION  
  
RUN gem install bundler  
  
RUN rbenv rehash  
  
# install go  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
# prepare go-env  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" "$GOPATH/pkg" && chmod -R 777
"$GOPATH"  
  
# install godep  
RUN go get github.com/tools/godep  
  
# install glide  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/0.10.2/glide-0.10.2-linux-
amd64.tar.gz  
ENV GLIDE_DOWNLOAD_SHA256
0eedb7f47ff4d184ab334f8dd8be843f8e98774b6ccd92cbe71a6e6c7a3d5da8  
  
RUN \  
curl -fsSL $GLIDE_DOWNLOAD_URL -o glide-inux-amd64.tar.gz && \  
tar xvf glide-inux-amd64.tar.gz && \  
mv linux-amd64/glide /usr/bin/ && \  
rm glide-inux-amd64.tar.gz && \  
rm -Rf linux-amd64  

