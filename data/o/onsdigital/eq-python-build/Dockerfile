FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y curl git wget locales python-pip make build-essential
libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev apt-transport-
https libpq-dev  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG=en_US.UTF-8  
RUN git clone git://github.com/yyuu/pyenv.git .pyenv  
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git
~/.pyenv/plugins/pyenv-virtualenv  
  
ENV HOME /  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
  
RUN pyenv install 3.4.2  
RUN pyenv global 3.4.2  
  
RUN pip install --upgrade pip setuptools pipenv  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
  
RUN apt-get update \  
&& apt-get install -y nodejs yarn google-chrome-stable  
  
# Function Test Dependencies  
# Install dependencies.  
RUN apt-get update && \  
apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4  
  

