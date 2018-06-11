FROM nvidia/cuda:6.5-devel  
  
MAINTAINER Wieland Brendel <wieland.brendel@posteo.de>  
  
# Copied from Jupyter/Notebook because packages cannot be removed once the  
# requirements for the Xserver are installed  
#  
# Remove preinstalled copy of python that blocks our ability to install
development python.  
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -yq \  
python3-minimal \  
python3.4 \  
python3.4-minimal \  
libpython3-stdlib \  
libpython3.4-minimal \  
libpython3.4-stdlib  
  
# Python binary and source dependencies  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq
--no-install-recommends \  
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
vim \  
wget \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install X11, SSH, sudo and gfortran  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq
--no-install-recommends \  
fluxbox \  
gfortran \  
openssh-server \  
pwgen \  
rox-filer \  
sudo \  
xdm \  
xpra \  
xserver-xephyr \  
xterm \  
xvfb  
  
# Build latest stable release from OpenBLAS from source  
ADD openblas.conf /etc/ld.so.conf.d/openblas.conf  
RUN mkdir /tmp/build  
  
RUN cd /tmp/build \  
&& git clone -q --branch=master https://github.com/xianyi/OpenBLAS.git  
  
RUN cd /tmp/build/OpenBLAS \  
&& make DYNAMIC_ARCH=1 NO_AFFINITY=1 NUM_THREADS=32 \  
&& make install DYNAMIC_ARCH=1 NO_AFFINITY=1 NUM_THREADS=32  
  
RUN rm -rf /tmp/build  
  
# Rebuild ld cache, this assumes that:  
# /etc/ld.so.conf.d/openblas.conf was installed by Dockerfile  
# and that the libraries are in /opt/OpenBLAS/lib  
RUN ldconfig  
  
# Configuring xdm to allow connections from any IP address and ssh to allow
X11 Forwarding.  
RUN sed -i 's/DisplayManager.requestPort/!DisplayManager.requestPort/g'
/etc/X11/xdm/xdm-config  
RUN sed -i '/#any host/c\\*' /etc/X11/xdm/Xaccess  
RUN ln -s /usr/bin/Xorg /usr/bin/X  
RUN echo X11Forwarding yes >> /etc/ssh/ssh_config  
  
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

