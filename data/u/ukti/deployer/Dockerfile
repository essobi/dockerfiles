FROM ubuntu:16.04  
ENV NVM_VER v0.33.8  
ENV CF_CLI_VER 6.36.0  
ENV OC_REL v3.7.0  
ENV OC_BUILD 7ed6862  
  
RUN groupadd -g 1000 ubuntu && \  
useradd -u 1000 -g 1000 -m -s /bin/bash ubuntu  
  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
apt-get update && \  
apt-get install -y curl wget git apt-transport-https ca-certificates software-
properties-common build-essential libpq-dev libssl-dev zlib1g-dev libbz2-dev
libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils
tk-dev postgresql-client && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y python3 python3-pip ruby-full rubygems bundler gettext jq
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -Lfs
"https://github.com/openshift/origin/releases/download/$OC_REL/openshift-
origin-client-tools-$OC_REL-$OC_BUILD-linux-64bit.tar.gz" | tar -xzf - -C
/usr/local/bin --strip 1 --wildcards */oc && \  
pip3 install --upgrade awscli virtualenv && \  
curl -Lfs https://cli-assets.heroku.com/install-ubuntu.sh | bash && \  
curl -Lfs https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key |
apt-key add - && \  
echo "deb https://packages.cloudfoundry.org/debian stable main" >
/etc/apt/sources.list.d/cloudfoundry-cli.list && \  
apt-get update && \  
apt-get install -y --allow-unauthenticated cf-cli=$CF_CLI_VER && \  
rm -rf /var/lib/apt/lists/*  
  
COPY Gemfile* /tmp/  
RUN gem install bundler && \  
bundle check || bundle install --gemfile=/tmp/Gemfile  
  
USER ubuntu:ubuntu  
ENV HOME /home/ubuntu  
  
RUN curl -Lfs https://raw.githubusercontent.com/pyenv/pyenv-
installer/master/bin/pyenv-installer | bash && \  
curl -Lfs https://raw.githubusercontent.com/creationix/nvm/$NVM_VER/install.sh
| bash && \  
gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB && \  
curl -Lfs https://get.rvm.io | bash && \  
bash -c "source ~/.rvm/scripts/rvm && rvm autolibs disable" && \  
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.profile && \  
echo 'eval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"' >> ~/.profile
&& \  
echo 'export NVM_DIR="$HOME/.nvm"\n[ -s "$NVM_DIR/nvm.sh" ] && \\.
"$NVM_DIR/nvm.sh"' >> ~/.profile && \  
cf install-plugin -f conduit  
  
ENTRYPOINT ["bash", "-c"]  

