FROM norionomura/swiftlint:swift-4.0.3  
RUN apt-get update && \  
apt-get install -y \  
bzip2 \  
libssl-dev \  
libreadline-dev \  
zlib1g-dev \  
unzip \  
openssh-client \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \  
&& git clone git://github.com/rbenv/ruby-build.git
/usr/local/rbenv/plugins/ruby-build \  
&& /usr/local/rbenv/plugins/ruby-build/install.sh  
ENV PATH /usr/local/rbenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \  
&& echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc  
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH  
  
ENV RBENV_VERSION 2.5.0  
RUN eval "$(rbenv init -)"; rbenv install $RBENV_VERSION \  
&& eval "$(rbenv init -)"; rbenv global $RBENV_VERSION \  
&& eval "$(rbenv init -)"; gem update --system \  
&& eval "$(rbenv init -)"; gem install bundler -f \  
&& rm -rf /tmp/*  
  
RUN gem install danger-gitlab danger-swiftlint danger-todoist  

