ARG centos_ver=7  
FROM centos:${centos_ver}  
LABEL maintainer="salihan <salihan04@gmail.com>"  
  
ARG ruby_ver=2.3.6  
ARG node_ver=8.9.3  
ENV RUBY_ENV=${ruby_ver} \  
NVM_DIR=/usr/local/nvm \  
NODE_VER=${node_ver} \  
NODE_PATH=$NVM_DIR/v$NODE_VER/lib/node_modules  
ENV PATH "${PATH}:/usr/local/nvm/versions/node/v${NODE_VER}/bin"  
ENV PATH "${PATH}:/usr/local/nvm/versions/node/v${NODE_VER}/bin/npm"  
  
RUN set -x \  
yum install epel-release \  
&& yum -y install libyaml libyaml-devel readline-devel ncurses-devel gdbm-
devel tcl-devel openssl-devel db4-devel libffi-devel which gpg gcc gcc-c++
make bind-utils \  
&& gpg \--keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB \  
|| (gpg \--keyserver hkp://pgp.mit.edu --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB && exit 1) \  
&& curl -L get.rvm.io | bash -s stable \  
&& yum clean all \  
&& /bin/bash -l -c "rvm requirements" \  
&& /bin/bash -l -c "rvm install ${RUBY_ENV}" \  
&& /bin/bash -l -c "rvm use ${RUBY_ENV} --default" \  
&& curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \  
&& /bin/bash -l -c ". ${NVM_DIR}/nvm.sh" \  
&& /bin/bash -l -c "nvm install ${NODE_VER}" \  
&& /bin/bash -l -c "nvm alias default ${NODE_VER}" \  
&& /bin/bash -l -c "nvm use default" \  
&& /bin/bash -l -c "echo \"[[ -s '/usr/local/rvm/bin/rvm' ]] && .
'/usr/local/rvm/bin/rvm'\" >> ~/.bashrc"  
  
ENV PATH "${PATH}:/usr/local/rvm/rubies/ruby-${RUBY_ENV}/bin"

