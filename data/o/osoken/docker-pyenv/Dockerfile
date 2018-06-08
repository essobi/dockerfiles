FROM buildpack-deps:jessie  
  
LABEL maintainer "osoken.devel@outlook.jp"  
  
ENV PYENV_ROOT=/usr/local/lib/pyenv  
ENV PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/yyuu/pyenv.git /usr/local/lib/pyenv \  
&& echo "export PYENV_ROOT=/usr/local/lib/pyenv" >> $HOME/.profile \  
&& echo "export PATH=$PYENV_ROOT/bin:$PATH" >> $HOME/.profile \  
&& echo 'eval "$(pyenv init -)"' >> $HOME/.profile  
  
ENTRYPOINT ["/bin/bash", "--login", "-i", "-c"]  
CMD ["bash"]  
  

