# Builds a Docker image with Ubuntu 16.04, Octave, Python3 and Jupyter
Notebook  
# for "AMS 595: Fundamental of Computing" at Stony Brook University  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
FROM compdatasci/octave-desktop:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
# Install system packages  
RUN add-apt-repository ppa:webupd8team/atom && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
gdb \  
ddd \  
valgrind \  
electric-fence \  
kcachegrind \  
ccache \  
libnss3 \  
nano \  
emacs \  
vim-gtk3 \  
\  
liblapack-dev \  
libopenblas-dev \  
libomp-dev \  
\  
meld \  
atom \  
clang \  
clang-format && \  
apt-get clean && \  
pip3 install -U \  
numpy \  
scipy \  
sympy \  
pandas \  
matplotlib \  
autopep8 \  
flake8 \  
PyQt5 \  
spyder && \  
echo "move_to_config atom" >> /usr/local/bin/init_vnc && \  
echo "move_to_config matlab/R2016b" >> /usr/local/bin/init_vnc && \  
echo "move_to_config matlab/R2017a" >> /usr/local/bin/init_vnc && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
########################################################  
# Customization for user  
########################################################  
ADD image/etc /etc  
ADD image/bin /usr/local/bin  
ADD image/home $DOCKER_HOME  
  
# Install gdutil and set permission  
RUN git clone \--depth 1 https://github.com/hpdata/gdutil /usr/local/gdutil &&
\  
pip2 install -r /usr/local/gdutil/requirements.txt && \  
pip3 install -r /usr/local/gdutil/requirements.txt && \  
ln -s -f /usr/local/gdutil/bin/* /usr/local/bin/ && \  
chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
USER $DOCKER_USER  
ENV GIT_EDITOR=vi EDITOR=atom  
RUN echo "@start_matlab" >> $DOCKER_HOME/.config/lxsession/LXDE/autostart && \  
echo 'export OMP_NUM_THREADS=$(nproc)' >> $DOCKER_HOME/.profile && \  
apm install \  
language-cpp14 \  
language-matlab \  
language-fortran \  
language-docker \  
autocomplete-python \  
autocomplete-fortran \  
git-plus \  
merge-conflicts \  
split-diff \  
gcc-make-run \  
platformio-ide-terminal \  
intentions \  
busy-signal \  
linter-ui-default \  
linter \  
linter-gcc \  
linter-gfortran \  
linter-flake8 \  
dbg \  
output-panel \  
dbg-gdb \  
python-debugger \  
auto-detect-indentation \  
python-autopep8 \  
clang-format && \  
rm -rf /tmp/* && \  
sed -i '/octave/ d' $DOCKER_HOME/.config/lxsession/LXDE/autostart && \  
echo "PATH=$DOCKER_HOME/bin:/usr/local/gdutil/bin:$PATH" >>
$DOCKER_HOME/.profile  
  
WORKDIR $DOCKER_HOME  
USER root  

