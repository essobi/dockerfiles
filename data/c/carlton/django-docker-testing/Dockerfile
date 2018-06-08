FROM python:3.6  
# Install Dependencies — See https://github.com/yyuu/pyenv/wiki/Common-build-
problems  
RUN apt-get update && apt-get install -y make build-essential libssl-dev
zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
libncurses5-dev libncursesw5-dev xz-utils  
  
# Install pyenv  
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
ENV PYENV_ROOT /root/.pyenv  
ENV PATH
/root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN pyenv install 2.7.10  
RUN pyenv install 3.3.6  
RUN pyenv install 3.4.6  
RUN pyenv install 3.5.3  
  
# Activate all installed Pythons  
RUN pyenv global system $(ls ~/.pyenv/versions/)  
  
RUN pip install tox  
RUN pip install detox  
  
# For the log...  
RUN pyenv versions

