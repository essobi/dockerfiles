FROM library/ubuntu:12.04  
RUN apt-get update && \  
apt-get install -y git curl bzip2 ssh tar gzip gcc autoconf bison \  
build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev \  
libncurses5-dev libffi-dev libgdbm3 libgdbm-dev apt-transport-https \  
postgresql libpq-dev pkg-config librsvg2-dev librsvg2-bin  
  
RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \  
&& git clone git://github.com/rbenv/ruby-build.git
/usr/local/rbenv/plugins/ruby-build \  
&& git clone git://github.com/jf/rbenv-gemset.git
/usr/local/rbenv/plugins/rbenv-gemset \  
&& /usr/local/rbenv/plugins/ruby-build/install.sh  
ENV PATH /usr/local/rbenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \  
&& echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc --enable-shared  
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH  
  
RUN eval "$(rbenv init -)"; rbenv install -v 2.4.2  
RUN eval "$(rbenv init -)"; rbenv install -v 2.4.3  
RUN eval "$(rbenv init -)"; rbenv install -v 2.5.0  
RUN mkdir -p "$(rbenv root)"/plugins  
RUN eval "$(rbenv init -)"; git clone https://github.com/rbenv/rbenv-each.git
"$(rbenv root)"/plugins/rbenv-each  
RUN eval "$(rbenv init -)"; rbenv each gem update --system  
RUN eval "$(rbenv init -)"; rbenv rehash  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get update && apt-get install -y nodejs yarn  
  
RUN curl -s -S -L
https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer
| bash  
RUN echo "[[ -s "$HOME/.gvm/scripts/gvm" ]] && source
\"$HOME/.gvm/scripts/gvm\"" >> ~/.bashrc  
RUN bash -c "source \"$HOME/.gvm/scripts/gvm\" && gvm install go1.9 -B && gvm
use go1.9 --default"  
  
RUN curl https://s3-eu-west-1.amazonaws.com/packages.altmetric.com/baller-1.1
-o /bin/baller && chmod +x /bin/baller  

