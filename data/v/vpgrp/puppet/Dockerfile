# Copyright (c) 2017, rockyluke  
#  
# Permission to use, copy, modify, and/or distribute this software for any  
# purpose with or without fee is hereby granted, provided that the above  
# copyright notice and this permission notice appear in all copies.  
#  
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH  
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY  
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,  
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM  
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR  
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR  
# PERFORMANCE OF THIS SOFTWARE.  
FROM centos:6  
ENV container="docker" \  
GEMS="/usr/local/rvm/gems/ruby-2.1.0" \  
RUBIES="/usr/local/rvm/rubies/ruby-2.1.0" \  
TZ="Europe/Amsterdam"  
RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm &&
\  
yum update -q -y && \  
yum install -q -y \  
redhat-lsb \  
sudo && \  
yum clean all -q  
  
# https://gist.github.com/slouma2000/8619039  
RUN mkdir -p /usr/local/rvm/config && \  
touch /usr/local/rvm/config/alias && \  
curl --location --silent 'https://rvm.io/mpapis.asc' | gpg2 --import - && \  
curl --location --silent 'http://get.rvm.io/' | bash -s stable  
  
# https://gist.github.com/konklone/6662393  
RUN bash -l -c 'rvm install 2.1.0' && \  
bash -l -c 'rvm --default use 2.1.0' && \  
bash -l -c 'gem install --no-rdoc --no-ri puppet --version 3.8.7'  
  
RUN ln -s ${RUBIES}/bin/gem /usr/bin/gem && \  
ln -s ${RUBIES}/bin/ruby /usr/bin/ruby  
  
ENV PATH="${RUBIES}/bin:${GEMS}/bin:${PATH}" \  
GEM_PATH="${GEMS}:${GEM_PATH}"  
# EOF  

