FROM ubuntu:16.04  
MAINTAINER ssaavedra  
  
ENV LANG en_US.UTF-8  
# Install git so that we can work with pbr-based projects  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git ca-certificates locales && \  
apt-get install -y --no-install-recommends \  
make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev
libsqlite3-dev llvm libncurses5-dev xz-utils \  
curl wget ca-certificates && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
  
ARG PYENV_REPO_VERSION=v1.1.3  
RUN git clone https://github.com/yyuu/pyenv.git --depth=50 .pyenv && (cd
.pyenv && git checkout $PYENV_REPO_VERSION)  
  
ENV PYENV_ROOT="/.pyenv" \  
PATH="/.pyenv/bin:/.pyenv/shims:$PATH"  
COPY python-versions.txt ./  
  
RUN xargs -P 4 -n 1 pyenv install < python-versions.txt && \  
pyenv global $(pyenv versions --bare) && \  
find $PYENV_ROOT/versions -type d '(' -name '__pycache__' -o -name 'test' -o
-name 'tests' ')' -exec rm -rfv '{}' \+ && \  
find $PYENV_ROOT/versions -type f '(' -name '*.py[co]' -o -name '*.exe' ')'
-exec rm -fv '{}' +  
  
RUN pyenv local 3.6.2 && \  
python -m pip install -U pip && \  
python -m pip install tox==2.7.0 && \  
pyenv local \--unset && \  
pyenv rehash  
  
WORKDIR /app  
VOLUME /src  
  
CMD ["tox"]  

