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
  
FROM rockyluke/debian:stretch  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
TZ="Europe/Amsterdam"  
  
RUN apt-get update -qq && \  
apt-get upgrade -qq -y && \  
apt-get install -qq -y \  
build-essential \  
dirmngr \  
lsb-release \  
puppet \  
ruby \  
ruby-dev \  
rubygems \  
sudo \  
systemd \  
zlib1g-dev && \  
apt-clean  
  
RUN gem install --no-document \--quiet rake --version 12.2.1 && \  
gem install --no-document \--quiet facter --version 2.4.6 && \  
gem install --no-document \--quiet jsonlint && \  
gem install --no-document \--quiet metadata-json-lint && \  
gem install --no-document \--quiet puppet --version 4.8.2 && \  
gem install --no-document \--quiet puppet-blacksmith && \  
gem install --no-document \--quiet puppet-lint && \  
gem install --no-document \--quiet puppet-syntax && \  
gem install --no-document \--quiet puppetlabs_spec_helper && \  
gem install --no-document \--quiet rails-erb-lint && \  
gem install --no-document \--quiet rspec-expectations && \  
gem install --no-document \--quiet rspec-puppet && \  
gem install --no-document \--quiet rubocop && \  
gem install --no-document \--quiet semantic_puppet && \  
gem install --no-document \--quiet serverspec && \  
gem install --no-document \--quiet yaml-lint  
  
ENV BUSSER_ROOT="/tmp/verifier" \  
GEM_HOME="/tmp/verifier/gems" \  
GEM_CACHE="/tmp/verifier/gems/cache" \  
GEM_PATH="/tmp/verifier/gems:${GEM_PATH}"  
  
RUN mkdir -p /tmp/verifier/bin && \  
gem install rake \  
\--version 12.2.1 \  
\--no-rdoc \  
\--no-ri \  
\--bindir /tmp/verifier/bin \  
\--quiet && \  
gem install busser \  
\--version 0.7.1 \  
\--no-rdoc \  
\--no-ri \  
\--bindir /tmp/verifier/bin \  
\--quiet && \  
gem install net-ssh \  
\--version 2.9.4 \  
\--no-rdoc \  
\--no-ri \  
\--bindir /tmp/verifier/bin \  
\--quiet && \  
gem install serverspec \  
\--version 2.41.3 \  
\--no-rdoc \  
\--no-ri \  
\--bindir /tmp/verifier/bin \  
\--quiet && \  
gem install busser-serverspec \  
\--version 0.5.10 \  
\--no-rdoc \  
\--no-ri \  
\--bindir /tmp/verifier/bin \  
\--quiet  
# EOF  

