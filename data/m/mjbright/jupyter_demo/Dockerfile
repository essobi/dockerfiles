# Docker demo image, as used on try.jupyter.org and tmpnb.org  
# github: jupyter/docker-demo-images  
FROM jupyter/demo  
  
MAINTAINER Michael Bright <github.com@mjbright.net>  
  
#USER root  
RUN apt-get update  
ENV PATH $CONDA_DIR/bin:$PATH  
  
# Ruby dependencies  
RUN apt-get install -y --no-install-recommends ruby ruby-dev libtool autoconf
automake gnuplot-nox libsqlite3-dev libatlas-base-dev libgsl0-dev && apt-get
clean  
# File already exists: && ln -s /usr/bin/libtoolize /usr/bin/libtool  
RUN apt-get install -y --no-install-recommends libmagick++-dev imagemagick  
RUN gem install --no-rdoc --no-ri sciruby-full  
  
USER jovyan  
  
#[datascience-notebook]# Install IJulia and Julia packages:  
#[datascience-notebook]RUN julia -e 'Pkg.add("IJulia")'  
#[datascience-notebook]RUN julia -e 'Pkg.add("Gadfly")' && julia -e
'Pkg.add("RDatasets")'  
# Install bash_kernel:  
# Make sure not to create a cache dir else NB_UID switching  
# will hit issues.  
RUN pip install --no-cache-dir bash_kernel && \  
python -m bash_kernel.install  
  
# Install RISE (LIVE Reveal) extension:  
RUN cd /home/jovyan && \  
mkdir -p /home/jovyan/src/git && \  
cd /home/jovyan/src/git && \  
git clone https://github.com/damianavila/RISE
/home/jovyan/src/git/damianvila.RISE && \  
cd /home/jovyan/src/git/damianvila.RISE && \  
python setup.py install  
  
USER root  
  
RUN groupadd -g 1000 docker && \  
usermod -a -G docker jovyan  
  
# Setup sudoers without password:  
ADD sudoers /etc/sudoers  
  
# Needed so notebooks can write to mounted work volume:  
RUN [ ! -d /home/jovyan/work ] && mkdir /home/jovyan/work; RET=0  
RUN chown jovyan /home/jovyan/work && chmod a+w /home/jovyan/work  
  
ADD docker /home/jovyan/work/docker  
  
# Install setup ssh:  
RUN apt-get install -y openssh-client  
RUN mkdir -p /home/jovyan/.ssh  
  
#### # Install setup xdot: (for graphical display of GraphViz)  
#### RUN apt-get install -y xdot  
USER jovyan  
  
# Install hide_code extension:  
# - original not Python3 - git clone https://github.com/kirbs-/hide_code && \  
RUN cd /home/jovyan/src/git && \  
git clone https://github.com/mjbright/hide_code && \  
cd /home/jovyan/src/git/hide_code && \  
python setup.py install  
  
# Install nbgrader extension:  
USER root  
RUN apt-get install -y pandoc  
USER jovyan  
RUN cd /home/jovyan/src/git && \  
git clone https://github.com/jupyter/nbgrader && \  
cd /home/jovyan/src/git/nbgrader && \  
python setup.py install  
  
ENV PATH /home/jovyan/.local/bin/:$PATH  
  
RUN nbgrader extension install --user --symlink && \  
nbgrader extension activate  
  
# Featured notebooks  
RUN git clone \--depth 1 https://github.com/jvns/pandas-cookbook.git
/home/jovyan/featured/pandas-cookbook/  
  
# Convert notebooks to the current format  
RUN find . -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output
{} \; ; echo  
RUN find . -name '*.ipynb' -exec ipython trust {} \; ; echo  
  
# Install Jessica Hamrick's PlotChecker module:  
RUN pip install plotchecker  
  
# Install MPDL3 library:  
RUN pip install mpld3  
  
# D3plot?:  
#RUN https://github.com/jdfreder/ipython-d3plot  
# Install bqplot module: FAILS with error:  
#  
#FIX?RUN sudo apt-get install -y libevent-dev python-dev build-essential  
#FIX?pip install uwsgi  
#RUN pip install bqplot  
#RUN python -m bqplot.install --symlink --user --force  
USER root  
  
# Add OpenStack nova client:  
# sudo -n apt-get install -y python-novaclient  
RUN apt-get install -y python-novaclient python-cinderclient python-
glanceclient python-neutronclient python-keystoneclient  
  

