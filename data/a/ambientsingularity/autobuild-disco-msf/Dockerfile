FROM ubuntu:14.04  
WORKDIR /opt  
USER root  
  
# Base packages  
RUN apt-get update && apt-get -y install \  
apache2 autoconf bash-completion bison build-essential curl gawk git git-core
iftop libapache2-mod-php5 \  
libapr1 libaprutil1 libcurl4-openssl-dev libevent-dev libffi-dev libgdbm-dev
libgmp3-dev \  
libncurses-dev libpcap-dev libpq-dev libreadline6-dev libssl-dev
libsqlite3-dev \  
libsvn1 libtool libxml2 libxml2-dev libxslt-dev libyaml-dev locate \  
nano nasm ncurses-dev nethogs nmap openssl proxychains postgresql postgresql-
client \  
postgresql-contrib python-crypto python-openssl python-pefile python-pexpect
python-pip python-pymssql \  
python-requests sqlite3 tar vim wget whois xsel zlib1g zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Python dependencies  
RUN pip install tabulate termcolor python-libnmap msgpack-python
beautifulsoup4 requests  
  
# startup script and tmux configuration file  
#COPY ./scripts/init.sh /usr/local/bin/init.sh && \  
RUN curl -sSL https://github.com/ambient-singularity/disco-
msf/raw/master/scripts/init.sh --output /usr/local/bin/init.sh && \  
chmod a+xr /usr/local/bin/init.sh  
  
## Updated tmux install & config  
RUN wget -qO-
https://github.com/tmux/tmux/releases/download/2.6/tmux-2.6.tar.gz | tar xvz  
WORKDIR tmux-2.6  
RUN ./configure && make -j"$(nproc)" && sudo make install  
  
## Cleanup tmux install  
WORKDIR /opt  
RUN rm -rf tmux-2.6/  
  
## Install tmux config  
RUN git clone https://github.com/samoshkin/tmux-config  
RUN tmux-config/install.sh && rm -r tmux-config  
  
## Install SEToolkit  
RUN git clone https://github.com/trustedsec/social-engineer-toolkit/ set/  
WORKDIR set  
RUN python setup.py install  
WORKDIR /opt  
RUN rm -r set/  
  
# Get Metasploit  
RUN git clone https://github.com/rapid7/metasploit-framework.git msf  
WORKDIR msf  
  
# Install PosgreSQL  
RUN curl -sSL https://github.com/ambient-singularity/disco-
msf/raw/master/scripts/db.sql --output /tmp/db.sql  
RUN /etc/init.d/postgresql start && su postgres -c "psql -f /tmp/db.sql"  
RUN curl -sSL https://github.com/ambient-singularity/disco-
msf/raw/master/config/database.yml --output /opt/msf/config/database.yml  
  
# RVM  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import  
RUN curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.3.1"  
RUN /bin/bash -l -c "rvm use 2.3.1 --default"  
RUN /bin/bash -l -c "source /usr/local/rvm/scripts/rvm"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN /bin/bash -l -c "source /usr/local/rvm/scripts/rvm && which bundle"  
RUN /bin/bash -l -c "which bundle"  
  
# Get dependencies  
RUN /bin/bash -l -c "BUNDLEJOBS=$(expr $(cat /proc/cpuinfo | grep vendor_id |
wc -l) \- 1)"  
RUN /bin/bash -l -c "bundle config --global jobs $BUNDLEJOBS"  
RUN /bin/bash -l -c "bundle install"  
  
# Install metasploithelper  
WORKDIR /tmp/data  
RUN git clone https://github.com/SpiderLabs/msfrpc  
WORKDIR /tmp/data/msfrpc/python-msfrpc  
RUN python setup.py install  
WORKDIR /root/.msf4/scripts/resource  
RUN git clone https://github.com/milo2012/metasploitHelper  
  
# Pull msf battery scripts  
WORKDIR /root/.msf4/scripts/resource  
RUN git clone https://github.com/kn0/battery  
RUN cp -r battery/* . && rm -r battery/battery/  
  
# Pull runall.rc ruby script  
RUN curl -sSl https://github.com/ambient-singularity/disco-
msf/raw/master/scripts/runall.rc --output
/root/.msf4/scripts/resource/runall.rc  
  
# Symlink tools to $PATH  
RUN for i in `ls /opt/msf/tools/*/*`; do ln -s $i /usr/local/bin/; done  
RUN ln -s /opt/msf/msf* /usr/local/bin  
  
# settings and custom scripts folder  
VOLUME /root/.msf4/  
VOLUME /tmp/data/  
  
# Custom .bashrc  
RUN wget https://raw.githubusercontent.com/ambient-singularity/disco-
msf/master/conf/.bashrc --output-file=/root/.bashrc  
  
# Starting script (DB + updates)  
CMD /usr/local/bin/init.sh  

