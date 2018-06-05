FROM debian:buster-slim  
LABEL maintainer "https://github.com/weiji14"  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ENV VER=stable  
  
# Setup base atom install  
RUN apt-get -qq update && apt-get install -y --no-install-recommends \  
# Install atom required dependencies  
git \  
gconf2 \  
gconf-service \  
libgtk2.0-0 \  
libnotify4 \  
libxtst6 \  
libnss3 \  
python \  
gvfs-bin \  
xdg-utils \  
libcap2 \  
# Install wget, ca-certificates  
wget \  
ca-certificates \  
# Install X11 and ALSA dependencies so we can view (and hear?) the atom GUI  
libx11-xcb1 \  
libxss1 \  
libasound2 \  
libxkbfile1 \  
# Install jupyter build required dependencies  
build-essential \  
python3-dev \  
python3-pip \  
# Get atom-amd64.deb release from https://atom.io/  
&& if [ "${VER}" = "stable" ]; \  
then wget --no-verbose https://atom.io/download/deb -O atom-amd64.deb; \  
elif [ "${VER}" = "beta" ]; \  
then wget --no-verbose https://atom.io/download/deb?channel=beta -O atom-
amd64.deb; \  
fi \  
# Finally install the 'base' atom-amd64 build  
&& dpkg -i atom-amd64.deb \  
&& rm -f atom-amd64.deb \  
# Install jupyter via pip3  
&& pip3 install setuptools wheel \  
&& pip3 install jupyter \  
# Remove dev/build stuff as not needed anymore  
&& apt-get remove -y \  
wget \  
build-essential \  
python3-dev \  
# More purging  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Initiate atom-editor with user 'atom'  
RUN useradd -d /home/atom -m atom  
USER atom  
  
# Setup atom directory  
RUN mkdir -p /home/atom/.atom  
RUN chmod 775 /home/atom/.atom  
RUN chown -R `whoami` /home/atom/.atom  
  
# Using apm to install hydrogen to /home/atom/.atom  
RUN if [ "${VER}" = "stable" ]; \  
then apm install hydrogen; \  
elif [ "${VER}" = "beta" ]; \  
then apm-beta install hydrogen; \  
fi  
  
# Initiate Jupyter config and start Jupyter notebook service  
RUN jupyter notebook --generate-config --no-browser  
  
# Fix 'No module named ipykernel_launcher'
https://github.com/nteract/hydrogen/issues/730  
RUN python3 -m ipykernel install --user  
  
RUN jupyter kernelspec list --json  
  
ENTRYPOINT ["/usr/bin/atom"]  
  
CMD ["-f"]

