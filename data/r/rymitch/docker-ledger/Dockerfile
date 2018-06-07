# Pull base image.  
FROM rymitch/docker-base  
  
# Install system packages.  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y install \  
cmake \  
doxygen \  
libboost-date-time-dev \  
libboost-dev \  
libboost-filesystem-dev \  
libboost-iostreams-dev \  
libboost-python-dev \  
libboost-regex-dev \  
libboost-system-dev \  
libboost-test-dev \  
libedit-dev \  
libgmp3-dev \  
libmpfr-dev \  
software-properties-common \  
texinfo \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install ledger.  
RUN cd /usr/local/src \  
&& git clone https://github.com/ledger/ledger.git \  
&& cd ledger \  
&& git checkout -b master origin/master \  
&& ./acprep update \  
&& make install  
  
# Install ledger-autosync.  
RUN cd /usr/local/src \  
&& git clone https://bitbucket.org/egh/ledger-autosync.git \  
&& cd ledger-autosync \  
&& python setup.py install  
  
# Install ledger-scripts.  
RUN cd /usr/local/src \  
&& git clone https://github.com/dpiddy/ledger-scripts.git \  
&& ln -s /usr/local/src/ledger-scripts/ledger-entry /usr/local/bin/ledger-
entry \  
&& ln -s /usr/local/src/ledger-scripts/ledger-sync /usr/local/bin/ledger-sync
\  
&& ln -s /usr/local/src/ledger-scripts/ledger-tidy /usr/local/bin/ledger-tidy  
  
# Install ledgerhub.  
RUN cd /usr/local/src \  
&& hg clone http://bitbucket.org/blais/ledgerhub \  
&& cd ledgerhub \  
&& python3 setup.py install  
  
# Set the data directory.  
ENV LEDGER_FILE /data/mitchell.dat  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

