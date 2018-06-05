FROM qixxit/elixir-centos:latest  
MAINTAINER Leif Gensert <leif@leif.io>  
  
RUN yum -y install \  
wget \  
jq  
  
ENV NODE_VERSION=8.5.0  
LABEL node_version=$NODE_VERSION  
  
RUN set -xe \  
cd /tmp \  
&& wget http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz \  
&& tar xzvf node-v* && cd node-v* \  
&& ./configure \  
&& make \  
&& make install  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
ENV PATH=/root/.yarn/bin/:$PATH  
  
RUN curl -O https://raw.githubusercontent.com/rockymadden/slack-
cli/master/src/slack \  
&& chmod +x slack \  
&& mv slack /usr/local/bin  
  
CMD ["/bin/sh"]  

