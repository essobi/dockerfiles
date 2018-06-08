# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER "Koji Shiraishi <shiraco@gmail.com>"  
# Install Python.  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install -y curl wget git build-essential openssl libssl-dev
zlib1g-dev bzip2  
RUN apt-get install -y tree grep sqlite3 libsqlite3-dev libreadline6-dev
libbz2-dev libssl-dev  
  
# Install python.  
ENV PYTHON_VERSION 3.5.2  
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv  
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile  
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile  
RUN echo 'eval "$(pyenv init -)"' >> ~/.bash_profile  
RUN ~/.pyenv/bin/pyenv install $PYTHON_VERSION  
RUN ~/.pyenv/bin/pyenv rehash  
RUN ~/.pyenv/bin/pyenv global $PYTHON_VERSION  
  
# Update pip to latest version.  
RUN ~/.pyenv/shims/pip install --upgrade pip  
  
# Install virtualenv.  
RUN ~/.pyenv/shims/pip install virtualenv  
  
# Install jupyter.  
RUN apt-get install -y pkg-config freetype* libfreetype6-dev libpng-dev dialog  
RUN ~/.pyenv/shims/pip install jupyter  
RUN ~/.pyenv/shims/jupyter notebook --generate-config && \  
~/.pyenv/shims/ipython profile create  
RUN echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py
&& \  
echo "c.NotebookApp.open_browser = False" >>
/root/.jupyter/jupyter_notebook_config.py && \  
echo "c.InteractiveShellApp.matplotlib = 'inline'" >>
/root/.ipython/profile_default/ipython_config.py  
RUN mkdir -p /root/notebook  
WORKDIR /root/notebook  
  
# Install dev tool.  
RUN apt-get install -y vim  
  
EXPOSE 8888  
# Define default command.  
CMD ["bash"]  

