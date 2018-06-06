FROM dit4c/dit4c-container-base:debian  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
# install  
# - Python 3, PIP and dependencies  
# - Xvfb for background X11 rendering  
# - matplotlib  
# - nltk.draw dependencies  
RUN apt-get update && \  
apt-get install -y \  
python3-pip python3-all-dev gfortran \  
libblas-dev liblapack-dev \  
libpng-dev libfreetype6-dev \  
libhdf5-dev \  
libnetcdf-dev \  
libyaml-dev \  
ghostscript imagemagick \  
xvfb \  
sqlite3 \  
python3-matplotlib \  
python3-tk && \  
apt-get clean  
  
RUN pip3 install --upgrade packaging appdirs  
RUN pip3 install ipython jupyter  
RUN pip3 install numpy pandas matplotlib gitpython  
RUN pip3 install scipy netCDF4  
RUN pip3 install numexpr cython  
RUN pip3 install tables  
RUN pip3 install seaborn  
  
COPY etc /etc  
COPY var /var  
  
RUN su - researcher -c "mkdir -p ~/.jupyter && echo -e
\"c.NotebookApp.base_url = '/jupyter'\nc.NotebookApp.token = ''\" >
~/.jupyter/jupyter_notebook_config.py"  

