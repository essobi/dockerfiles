# Builds a Docker image with Ubuntu 17.10, g++-7.2, clang, Atom, LAPACK, ddd,  
# valgrind, and mpich for "AMS 562: Introduction to Scientific Programming in
C++"  
# at Stony Brook University  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
  
FROM x11vnc/desktop:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
ADD image/home $DOCKER_HOME/  
# Install system packages  
RUN add-apt-repository ppa:webupd8team/atom && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
gfortran \  
cmake \  
bison \  
flex \  
doxygen \  
git \  
bash-completion \  
bsdtar \  
rsync \  
wget \  
gdb \  
ddd \  
valgrind \  
electric-fence \  
ccache \  
\  
liblapack-dev \  
liblapacke-dev \  
libmpich-dev \  
libopenblas-dev \  
mpich \  
libomp-dev \  
\  
meld \  
atom \  
clang \  
clang-format && \  
apt-get clean && \  
echo "move_to_config atom" >> /usr/local/bin/init_vnc && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
########################################################  
# Customization for user  
########################################################  
  
ENV GIT_EDITOR=vi EDITOR=atom  
COPY WELCOME $DOCKER_HOME/WELCOME  
  
RUN apm install \  
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
dbg \  
output-panel \  
dbg-gdb \  
auto-detect-indentation \  
clang-format && \  
rm -rf /tmp/* && \  
echo '@atom .' >> $DOCKER_HOME/.config/lxsession/LXDE/autostart && \  
chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
WORKDIR $DOCKER_HOME  

