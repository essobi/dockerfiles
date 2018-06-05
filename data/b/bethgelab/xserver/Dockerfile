FROM ubuntu:14.04  
  
MAINTAINER Bethge Lab <opensource@bethgelab.org>  
  
# set the time zone correctly  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
  
# Copied from Jupyter/Notebook because packages cannot be removed once the  
# requirements for the Xserver are installed  
# (small modification in the last line)  
# ---- BEGIN ----  
# ---- MODIFICATION BEGIN ----  
# Not essential, but wise to set the lang  
# Note: Users with other languages should set this in their derivative image  
#ENV LANGUAGE en_US.UTF-8  
#ENV LANG en_US.UTF-8  
#ENV LC_ALL en_US.UTF-8  
#ENV PYTHONIOENCODING UTF-8  
# ---- MODIFICATION END ----  
# Remove preinstalled copy of python that blocks our ability to install
development python.  
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -yq \  
python3-minimal \  
python3.4 \  
python3.4-minimal \  
libpython3-stdlib \  
libpython3.4-stdlib \  
libpython3.4-minimal  
  
# Python binary and source dependencies  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
language-pack-en \  
libcurl4-openssl-dev \  
libffi-dev \  
libsqlite3-dev \  
libzmq3-dev \  
pandoc \  
python \  
python3 \  
python-dev \  
python3-dev \  
sqlite3 \  
texlive-fonts-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ---- END ----  
# use https:// instead of git:// to access github (e.g. for jupyter install)  
RUN git config --global url.https://github.com/.insteadOf git://github.com/  
  
# Install X11, SSH, sudo and gfortran, etc.  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq
--no-install-recommends \  
fluxbox \  
gfortran \  
openssh-server \  
pwgen \  
rox-filer \  
screen \  
sudo \  
tmux \  
vim \  
wget \  
xdm \  
xpra \  
xserver-xephyr \  
xterm \  
xvfb \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Build latest stable release from OpenBLAS from source  
#  
# Rebuild ld cache, this assumes that:  
# /etc/ld.so.conf.d/openblas.conf was installed by Dockerfile  
# and that the libraries are in /opt/OpenBLAS/lib  
ADD openblas.conf /etc/ld.so.conf.d/openblas.conf  
RUN mkdir /tmp/build \  
&& cd /tmp/build \  
&& git clone -q --branch=master https://github.com/xianyi/OpenBLAS.git \  
&& cd /tmp/build/OpenBLAS \  
&& make DYNAMIC_ARCH=1 NO_AFFINITY=1 NUM_THREADS=32 \  
&& make install DYNAMIC_ARCH=1 NO_AFFINITY=1 NUM_THREADS=32 \  
&& rm -rf /tmp/build \  
&& ldconfig  
  
# Configuring xdm to allow connections from any IP address and ssh to allow
X11 Forwarding.  
RUN sed -i 's/DisplayManager.requestPort/!DisplayManager.requestPort/g'
/etc/X11/xdm/xdm-config \  
&& sed -i '/#any host/c\\*' /etc/X11/xdm/Xaccess \  
&& ln -s /usr/bin/Xorg /usr/bin/X \  
&& echo X11Forwarding yes >> /etc/ssh/ssh_config  
  
# Fix PAM login issue with sshd  
RUN sed -i 's/session required pam_loginuid.so/#session required
pam_loginuid.so/g' /etc/pam.d/sshd  
# Set locale (fix the locale warnings)  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
  
# Expose SSH port  
EXPOSE 22  
  
# Create the directory needed to run the sshd daemon  
RUN mkdir /var/run/sshd  
  
# restarts the xdm service  
RUN /etc/init.d/xdm restart  
  
# Copy the config files into the docker directory  
COPY bin/* /usr/local/bin/  
  
# Start the ssh service  
CMD bash -C '/usr/local/bin/run'  

