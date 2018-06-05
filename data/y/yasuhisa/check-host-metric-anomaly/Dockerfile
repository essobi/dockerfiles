FROM ubuntu  
MAINTAINER Yasuhisa Yoshida <syou6162@gmail.com>  
  
ENV PYENV_ROOT /root/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
  
RUN apt-get update && \  
apt-get install -y git mercurial build-essential libssl-dev libbz2-dev
libreadline-dev libsqlite3-dev curl jq tk-dev && \  
curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
RUN pyenv install 3.6.0  
RUN pyenv global 3.6.0  
  
RUN pyenv rehash  
RUN pip install \  
numpy \  
scipy \  
scikit-learn \  
matplotlib \  
pandas \  
mackerel.clienthde  
  
RUN echo "backend : Agg" > /etc/matplotlibrc  
  
ENV APP_PATH="/app"  
WORKDIR ${APP_PATH}  
COPY . ${APP_PATH}  

