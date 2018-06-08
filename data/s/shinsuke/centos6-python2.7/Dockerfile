FROM centos:6  
MAINTAINER OTSUKI Shinsuke  
RUN yum groupinstall -y "Development tools"  
RUN yum install -y zlib-devel  
RUN yum install -y bzip2-devel  
RUN yum install -y openssl-devel  
RUN yum install -y ncurses-devel  
RUN yum install -y sqlite-devel  
RUN yum install -y mysql mysql-devel  
RUN yum install -y tar  
RUN echo "root:root" | chpasswd  
RUN cd /opt \  
&& curl --remote-name
https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz \  
&& tar xf Python-3.4.2.tar.xz \  
&& cd Python-3.4.2 \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make altinstall  
RUN useradd app  
USER app  
WORKDIR /home/app  
ENV HOME /home/app  
ENV PYENV_ROOT /home/app/pyenv  
RUN /usr/local/bin/pyvenv-3.4 /home/app/pyenv  
RUN source ./pyenv/bin/activate  
RUN echo 'export PYENV_ROOT="/home/app/pyenv"' >> ~/.bashrc  
RUN echo 'if [ -d "${PYENV_ROOT}" ]; then' >> ~/.bashrc  
RUN echo ' export PATH=${PYENV_ROOT}/bin:$PATH' >> ~/.bashrc  
RUN echo ' eval "$(/bin/bash ${PYENV_ROOT}/bin/activate)"' >> ~/.bashrc  
RUN echo 'fi' >> ~/.bashrc  
RUN $PYENV_ROOT/bin/pip install django  
RUN $PYENV_ROOT/bin/pip install mysqlclient  
RUN $PYENV_ROOT/bin/pip install readline  
RUN $PYENV_ROOT/bin/pip install uwsgi  
CMD /bin/bash  

