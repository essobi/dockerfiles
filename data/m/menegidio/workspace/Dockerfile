FROM menegidio/dugongworkspace  
MAINTAINER Fabiano Menegidio  
  
ENV HOME /home/dugong  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH
$HOME/.pyenv/shims:$HOME/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
ADD .config/scripts/.bashrc $HOME/.bashrc  
ADD .config/scripts/.bash_profile $HOME/.bash_profile  
  
RUN git clone git://github.com/yyuu/pyenv.git $PYENV_ROOT \  
&& git clone https://github.com/yyuu/pyenv-virtualenv.git
$PYENV_ROOT/plugins/pyenv-virtualenv \  
&& cd $HOME \  
&& /bin/bash -c "source $HOME/.bash_profile" \  
&& /bin/bash -c "source $HOME/.bashrc" \  
&& eval "$(pyenv init -)" \  
&& eval "$(pyenv virtualenv-init -)" \  
&& pyenv install miniconda3-latest \  
&& pyenv activate miniconda3-latest \  
&& conda config --add channels defaults && conda config --add channels conda-
forge \  
&& conda config --add channels r && conda config --add channels bioconda \  
&& conda update --all && conda clean -tipsy \  
&& pyenv deactivate  

