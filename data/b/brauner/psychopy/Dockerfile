FROM brauner/debian:stable  
  
MAINTAINER Christian Brauner christianvanbrauner[at]gmail.com  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& export DEBCONF_NONINTERACTIVE_SEEN=true \  
&& export DEBCONF_DB_OVERRIDE=File{/root/dat} \  
&& cd /root \  
&& printf '\nName: jackd/tweak_rt_limits\nTemplate:
jackd/tweak_rt_limits\nValue: true\nOwners: jackd2\n' > dat \  
&& printf 'set editing-mode vi\n\nset keymap vi-command\n' > .inputrc \  
&& cd /etc/dpkg/dpkg.cfg.d \  
&& printf '\npath-exclude=/usr/share/locale/*' >> excludes \  
&& printf '\npath-include=/usr/share/locale/en*' >> excludes \  
&& printf '\npath-include=/usr/share/locale/locale.alias' >> excludes \  
&& printf '\npath-exclude=/usr/share/man/*' >> excludes \  
&& printf '\npath-include=/usr/share/man/en*' >> excludes \  
&& printf '\npath-include=/usr/share/man/man[1-9]/*' >> excludes \  
&& cd /etc/apt/sources.list.d \  
&& printf '\ndeb http://neurodebian.g-node.org data main contrib non-free' >
neurodebian.sources.list \  
&& printf '\ndeb-src http://neurodebian.g-node.org data main contrib non-free'
>> neurodebian.sources.list \  
&& printf '\ndeb http://neurodebian.g-node.org wheezy main contrib non-free'
>> neurodebian.sources.list \  
&& printf '\ndeb-src http://neurodebian.g-node.org wheezy main contrib non-
free\n' >> neurodebian.sources.list \  
&& apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 2649A5A9 \  
&& apt-get update -qq -y \  
&& apt-get install -y --no-install-recommends \  
# Sound  
alsa-base \  
alsa-utils \  
alsa-oss \  
bash-completion \  
bzip2 \  
ca-certificates \  
gcc \  
g++ \  
gfortran \  
git \  
locales \  
less \  
make \  
mupdf \  
patch \  
sudo \  
wget \  
zip \  
unzip \  
# 3D  
i965-va-driver \  
libegl1-mesa \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libopenvg1-mesa \  
libglu1-mesa-dev \  
mesa-utils \  
# Sound  
alsa-base \  
alsa-utils \  
alsa-oss \  
flac \  
# Psychopy deps  
dbus \  
dbus-x11 \  
iceweasel \  
jackd \  
jackd2 \  
libavbin-dev \  
libavbin0 \  
libusb-1.0-0 \  
libusb-1.0-0-dev \  
python \  
python-setuptools \  
python-numpy \  
python-scipy \  
python-pyglet \  
python-wxgtk2.8 \  
python-wxtools \  
python-wxversion \  
python-imaging \  
python-matplotlib \  
python-lxml \  
python-openpyxl \  
python-pyo \  
# Psychopy opt deps  
python-optcomplete \  
python-pypsignifit \  
python-parallel \  
python-pp \  
python-pytest \  
python-serial \  
python-sphinx \  
python-tk \  
xdg-utils \  
&& dpkg-reconfigure -p high jackd2 \  
&& echo 'root:test' | chpasswd \  
&& useradd -u 1000 -m docker \  
&& echo 'docker:test' | chpasswd \  
&& usermod -s /bin/bash docker \  
&& usermod -a -G 100 docker \  
&& usermod -a -G sudo docker \  
&& groupmod -g 91 video \  
&& usermod -a -G video docker \  
&& groupmod -g 92 audio \  
&& usermod -a -G audio docker \  
&& cd /etc \  
&& printf '\nen_IE.UTF-8 UTF-8\n' >> locale.gen \  
&& locale-gen \  
&& cd /root \  
# && printf '# If not running interactively, don'\''t do anything\n[[ \$- !=
*i* ]] && return\n\nalias ls='\''ls --color=auto'\''\n\nalias grep='\''grep
--color=auto'\''\n\nPS1='\''[\\u@\h \W]\\$ '\''\n\ncomplete -cf sudo\n\n# Set
default editor.\nexport EDITOR=vim xterm\n\n# Enable vi editing mode.\nset -o
vi\n' > /root/.bashrc \  
&& printf 'set editing-mode vi\n\nset keymap vi-command\n' > .inputrc \  
&& rm -f dat \  
&& cd /home/docker \  
# && printf '# If not running interactively, don'\''t do anything\n[[ \$- !=
*i* ]] && return\n\nalias ls='\''ls --color=auto'\''\n\nalias grep='\''grep
--color=auto'\''\n\nPS1='\''[\\u@\h \W]\\$ '\''\n\ncomplete -cf sudo\n\n# Set
default editor.\nexport EDITOR=vim xterm\n\n# Enable vi editing mode.\nset -o
vi\n' > /home/docker/.bashrc \  
&& printf 'set editing-mode vi\n\nset keymap vi-command\n' > .inputrc \  
# exodriver for LabJack  
&& cd /home/docker \  
&& git clone git://github.com/labjack/exodriver.git \  
&& cd exodriver \  
&& ./install.sh \  
&& usermod -a -G adm docker \  
# LabJack  
&& cd /home/docker \  
&& git clone https://github.com/labjack/LabJackPython.git \  
&& cd LabJackPython \  
&& python setup.py install \  
&& cd /home/docker \  
&& git clone https://github.com/psychopy/psychopy.git \  
&& cd psychopy \  
&& python setup.py install \  
&& apt-get clean \  
&& cd /var/lib/apt/lists \  
&& rm -rf *  
  
ENV LANG en_IE.UTF-8  
ENV HOME /home/docker  
WORKDIR /home/docker  
USER docker  

