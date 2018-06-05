# The docker image `abeja/amazonlinux-elixir-awscli` includes:  
#  
# - Elixir 1.6.1  
# - Node.js 6  
# - awscli  
#  
# https://hub.docker.com/r/abeja/amazonlinux-elixir-node-awscli/  
FROM amazonlinux  
  
RUN set -xe \  
&& yum -y install git \  
&& yum -y groupinstall "Development Tools" \  
&& yum -y install ncurses-devel openssl-devel  
  
# Erlang  
RUN set -xe \  
&& curl -LO http://erlang.org/download/otp_src_20.1.tar.gz \  
&& tar -zxvf otp_src_20.1.tar.gz \  
&& rm -rf otp_src_20.1.tar.gz \  
&& cd otp_src_20.1/ \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf otp_src_20.1 \  
&& find /usr/local -name examples | xargs rm -rf  
  
# Elixir  
ENV LANG="en_US.utf8" LANGUAGE="en_US:" LC_ALL=en_US.UTF-8  
RUN set -xe \  
&& curl -LO https://github.com/elixir-
lang/elixir/releases/download/v1.6.1/Precompiled.zip \  
&& unzip Precompiled.zip -d /opt/elixir \  
&& rm -rf Precompiled.zip  
  
ENV PATH /opt/elixir/bin:$PATH  
  
# Node  
RUN set -xe \  
&& curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - \  
&& yum -y install nodejs  
  
# awscli  
RUN set -xe \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli --upgrade  
  
CMD ["bin/bash"]  

