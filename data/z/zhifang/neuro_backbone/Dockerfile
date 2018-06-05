FROM ubuntu:xenial  
MAINTAINER Zhifang Ye <zhifang.ye.fghm@gmail.com>  
  
#------------------------------------------------------------------------------  
# Basic Preparation and ENV variables  
#------------------------------------------------------------------------------  
ARG DEBIAN_FRONTEND=noninteractive  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
#------------------------------------------------------------------------------  
# Install common softwares  
#------------------------------------------------------------------------------  
RUN apt-get update -qq && apt-get upgrade -yq  
RUN apt-get install -qq apt-utils language-pack-en-base lsb-release sudo
gdebi-core \  
git curl wget tar bzip2 unzip filezilla \  
xvfb tcsh zsh ca-certificates net-tools \  
build-essential cmake cmake-curses-gui automake autoconf libtool gcc gfortran
g++ \  
tzdata htop terminator vim nano pandoc \  
mesa-utils libgl1-mesa-dev libglu1-mesa-dev libglw1-mesa-dev \  
libgtk2.0-dev libgtk-3-dev freeglut3-dev  
  
#------------------------------------------------------------------------------  
# Install neuro-softwares dependencies  
#------------------------------------------------------------------------------  
# FSL  
RUN apt-get update -qq \  
&& apt-get install -qq libatk-adaptor libgail-common \  
libcanberra-gtk-module topmenu-gtk2 topmenu-gtk3 libjpeg62-dev adwaita-icon-
theme-full \  
&& apt-get install -qq libmng2  
# AFNI  
RUN apt-get update -qq \  
&& apt-get install -qq xfonts-base python-qt4 gsl-bin netpbm gnome-tweak-tool
\  
libxm4 libnlopt-dev  
# SPM  
RUN apt-get update -qq \  
&& apt-get install -qq libxext6 libxt6  
# PyMVPA2  
RUN apt-get update -qq \  
&& apt-get install -qq swig  
# ASHS  
RUN apt-get update -qq \  
&& apt-get install -qq imagemagick  
# RStudio Server  
RUN apt-get update -qq \  
&& apt-get install -qq libapparmor1 libedit2 libc6 psmisc rrdtool  
  
#------------------------------------------------------------------------------  
# Cleanup  
#------------------------------------------------------------------------------  
RUN apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#------------------------------------------------------------------------------  
# Install oh my zsh and change default shell to zsh  
#------------------------------------------------------------------------------  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& chsh -s /bin/zsh  
  
#------------------------------------------------------------------------------  
# Change timezone to Shanghai  
#------------------------------------------------------------------------------  
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
#------------------------------------------------------------------------------  
# Setup git account  
#------------------------------------------------------------------------------  
RUN git config --global user.name "Zhifang Ye" \  
&& git config --global user.email zhifang.ye.fghm@gmail.com  
  
ENTRYPOINT ["/bin/zsh"]  

