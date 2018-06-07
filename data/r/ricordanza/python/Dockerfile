FROM ricordanza/develop  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
apt-get install -y python python-pip zlib1g-dev libsqlite3-dev tk-dev
libbz2-dev libreadline-dev libssl-dev openssl && \  
pip install --upgrade pip && \  
pip install virtualenv ipython && \  
echo "WORKON_HOME=~/.virtualenvs" >> ~/.bashrc && \  
git clone https://github.com/yyuu/pyenv.git ~/.pyenv && \  
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-
virtualenv && \  
echo 'export PYENV_ROOT=$HOME/.pyenv' >> ~/.bashrc && \  
echo 'export PATH=$PYENV_ROOT/bin:$PATH' >> ~/.bashrc && \  
echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \  
echo 'eval "$(pyenv init -)"' >> /etc/profile && \  
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc && \  
echo 'eval "$(pyenv virtualenv-init -)"' >> /etc/profile && \  
eval "$(~/.pyenv/bin/pyenv init -)" && \  
eval "$(~/.pyenv/bin/pyenv virtualenv-init -)" && \  
~/.pyenv/bin/pyenv install 3.6.1 && \  
~/.pyenv/bin/pyenv global 3.6.1 && \  
~/.pyenv/bin/pyenv rehash && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

