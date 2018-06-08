FROM ubuntu:latest  
MAINTAINER Fabiano Menegidio <fabiano.menegidio@biology.bio.br>  
  
############### Environment config  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --allow-unauthenticated git build-
essential locales ca-certificates vim \  
openssh-server curl python libssl-dev libreadline-dev zlib1g-dev  
  
ENV PASS dugong  
ENV USER dugong  
ENV HOME /headless  
  
RUN echo "User: $USER Pass: $PASS" \  
&& useradd -d $HOME \--shell /bin/bash --user-group --groups adm,sudo $USER \  
&& echo "$USER:$PASS" | chpasswd \  
&& echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& mkdir -p $HOME/data \  
&& mkdir -p $HOME/.ve \  
&& mkdir -p $HOME/.workspace \  
&& ln -s $HOME/.ve $HOME/data/.ve && ln -s $HOME/.workspace
$HOME/data/.workspace \  
&& chown -R $USER:$USER $HOME  
  
USER $USER  
WORKDIR $HOME  
  
##################### INSTALL PYTHON, PERL AND RUBY ENVIRONMENT (pyenv, plenv
and rbenv)  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PLENV_ROOT $HOME/.plenv  
ENV RBENV_ROOT $HOME/.rbenv  
ENV NB_USER $USER  
ENV NB_PASS $PASS  
ENV NB_UID 1000  
ENV CONDA3_DIR $PYENV_ROOT/versions/miniconda3-latest/  
ENV CONDA2_DIR $PYENV_ROOT/versions/miniconda2-latest/  
ENV PATH
$HOME/.plenv:$HOME/.pyenv/shims:$HOME/.pyenv/bin:$HOME/.plenv:$HOME/.plenv/bin:$HOME/.plenv/shims:$HOME/.rbenv/bin:$HOME/.rbenv:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
ADD .config/scripts/.bashrc $HOME/.bashrc  
ADD .config/scripts/.bash_profile $HOME/.bash_profile  
  
RUN git clone git://github.com/yyuu/pyenv.git $PYENV_ROOT \  
&& git clone https://github.com/yyuu/pyenv-virtualenv.git
$PYENV_ROOT/plugins/pyenv-virtualenv \  
&& git clone https://github.com/tokuhirom/plenv.git $PLENV_ROOT \  
&& git clone https://github.com/tokuhirom/Perl-Build.git
$PLENV_ROOT/plugins/perl-build/ \  
&& git clone https://github.com/rbenv/rbenv.git $RBENV_ROOT \  
&& git clone https://github.com/rbenv/ruby-build.git $RBENV_ROOT/plugins/ruby-
build \  
&& git clone \--depth 1 git://github.com/jf/rbenv-gemset.git
$RBENV_ROOT/plugins/rbenv-gemset \  
&& cd $HOME \  
&& /bin/bash -c "source $HOME/.bash_profile" \  
&& /bin/bash -c "source $HOME/.bashrc" \  
&& eval "$(pyenv init -)" \  
&& eval "$(pyenv virtualenv-init -)" \  
&& eval "$(rbenv init -)" \  
&& pyenv install miniconda3-latest \  
&& pyenv install miniconda2-latest \  
&& pyenv global miniconda3-latest miniconda2-latest \  
&& pyenv activate miniconda3-latest \  
&& conda config --add channels defaults && conda config --add channels conda-
forge \  
&& conda config --add channels r && conda config --add channels bioconda \  
&& conda update --all && conda clean -tipsy \  
&& pyenv deactivate \  
&& pyenv activate miniconda2-latest \  
&& conda config --add channels defaults && conda config --add channels conda-
forge \  
&& conda config --add channels r && conda config --add channels bioconda \  
&& conda update --all && conda clean -tipsy \  
&& conda install biopython \  
&& pyenv deactivate \  
&& pyenv global miniconda3-latest miniconda2-latest \  
&& plenv install 5.27.2 \  
&& plenv global 5.27.2 \  
&& rbenv install 2.4.1 \  
&& rbenv global 2.4.1 \  
&& pyenv rehash && plenv rehash && rbenv rehash  
  
USER root  
  
##################### Expose ports  
######### Jupyter Notebook  
EXPOSE 8888  
######### SSH Protocol  
EXPOSE 22  
VOLUME ["$HOME/data"]  
CMD ["/bin/bash"]  
  
USER $USER  
WORKDIR $HOME/data  

