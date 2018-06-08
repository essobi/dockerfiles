FROM debian:jessie  
  
MAINTAINER Malte Krupa <dockerfile@nafn.de>  
  
# Prepare python environment  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
pkg-config \  
python \  
python-pip \  
python-dev \  
build-essential \  
make \  
gcc \  
locales  
  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
  
RUN apt-get update && apt-get install -y \  
pandoc \  
libfreetype6 \  
libfreetype6-dev \  
libatlas-base-dev \  
gfortran \  
octave \  
libzmq3-dev \  
epstool \  
xfig \  
libblas3  
  
RUN pip install numpy scipy  
RUN pip install matplotlib Pygments oct2py ipython[notebook]  
  
ADD ipython.py /ipython.py  
RUN chmod o+x /ipython.py  
  
RUN groupadd -r ipython && \  
useradd -m -r -g ipython -s /sbin/nologin -c "ipython user" ipython && \  
mkdir /ipython && \  
chown -R ipython: /ipython  
  
USER ipython  
ENV HOME /home/ipython  
RUN ipython profile create && \  
echo "c.FileNotebookApp.notebook_dir = u'/ipython'" >> \  
$HOME/.ipython/profile_default/ipython_notebook_config.py  
  
RUN python -c \  
"from IPython.external import mathjax; mathjax.install_mathjax()"  
  
VOLUME ["/ipython"]  
EXPOSE 8888  
WORKDIR /ipython  
  
CMD /ipython.py  

