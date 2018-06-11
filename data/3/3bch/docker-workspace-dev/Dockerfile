FROM 3bch/docker-workspace-java:ubuntu-LTS  
MAINTAINER 3bch  
  
# Install Clang  
RUN apt-get install -y make clang  
  
# Install Rust  
RUN zsh -c "sh <(curl -sSf https://sh.rustup.rs) -y"  
  
# Install Node.js  
RUN curl -L git.io/nodebrew | perl - setup  
RUN set -x && \  
/root/.nodebrew/current/bin/nodebrew install-binary latest && \  
/root/.nodebrew/current/bin/nodebrew use latest  
  
# Install Miniconda  
SHELL ["/bin/bash", "-c"]  
RUN set -x && \  
git clone \--depth 1 https://github.com/yyuu/pyenv.git /root/.pyenv && \  
export PYENV_ROOT=/root/.pyenv && \  
export PATH=$PYENV_ROOT/bin:$PATH && \  
eval "$(pyenv init -)" && \  
export ANACONDA_VERSION=$(pyenv install -l | grep miniconda3 | tail -n 1 | tr
-d " ") && \  
pyenv install $ANACONDA_VERSION && \  
pyenv rehash && \  
pyenv global $ANACONDA_VERSION && \  
conda update -y conda && \  
conda install -y scikit-learn  
  
# Copy Zsh Config  
COPY ./zsh /root/.zsh  
RUN set -x && \  
echo ". ~/.zsh/path.zsh" >> /root/.zshrc && \  
/root/.cargo/bin/rustup completions zsh > /root/.zsh/scripts/_rustup  
  

