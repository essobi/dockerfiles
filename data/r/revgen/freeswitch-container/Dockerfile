# Jenkins.  
FROM ubuntu:14.04  
MAINTAINER Michal @ Revolution Generation <michal@revolutiongeneration.co.uk>  
  
# Enable the Ubuntu multiverse repository.  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/source.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty multiverse">>
/etc/apt/source.list  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates multiverse"
>> /etc/apt/source.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates
multiverse" >> /etc/apt/source.list  
# Enable videolan stable repository.  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:videolan/stable-daily  
  
# Install Dependencies.  
RUN apt-get update && apt-get install -y autoconf automake bison build-
essential fail2ban gawk git-core groff groff-base erlang-dev libasound2-dev
libavcodec-dev libavutil-dev libavformat-dev liba52-0.7.4-dev libdb-dev
libexpat1-dev libcurl4-openssl-dev libgdbm-dev libgnutls-dev libjpeg-dev
libmp3lame-dev libncurses5 libncurses5-dev libperl-dev libogg-dev libsnmp-dev
libssl-dev libtiff4-dev libtool libvorbis-dev libx11-dev libzrtpcpp-dev make
portaudio19-dev python-dev snmp snmpd subversion unixodbc-dev uuid-dev
zlib1g-dev libsqlite3-dev libpcre3-dev libspeex-dev libspeexdsp-dev libldns-
dev libedit-dev libladspa-ocaml-dev libmemcached-dev libmp4v2-dev libmyodbc
libpq-dev libvlc-dev libv8-dev liblua5.2-dev libyaml-dev libpython-dev odbc-
postgresql sendmail unixodbc wget yasm  
  
# Use Gawk.  
RUN update-alternatives --set awk /usr/bin/gawk  
  
# Install source code dependencies.  
ADD build/install-deps.sh /root/install-deps.sh  
WORKDIR /root  
RUN chmod +x install-deps.sh  
RUN ./install-deps.sh  
RUN rm install-deps.sh  
  
# Configure Fail2ban  
ADD conf/fail2ban/freeswitch.conf /etc/fail2ban/filter.d/freeswitch.conf  
ADD conf/fail2ban/freeswitch-dos.conf /etc/fail2ban/filter.d/freeswitch-
dos.conf  
ADD conf/fail2ban/jail.local /etc/fail2ban/jail.local  
  
# Download FreeSWITCH.  
WORKDIR /usr/src  
ENV GIT_SSL_NO_VERIFY=1  
RUN git clone https://freeswitch.org/stash/scm/fs/freeswitch.git -b v1.6  
  
# Bootstrap the build.  
WORKDIR freeswitch  
RUN ./bootstrap.sh  
  
# Enable the desired modules.  
ADD build/modules.conf /usr/src/freeswitch/modules.conf  
  
# Build FreeSWITCH.  
RUN ./configure --enable-core-pgsql-support  
RUN make  
RUN make install  
RUN make cd-sounds-install  
RUN make cd-moh-install  
  
# Configure Freeswitch  
COPY conf/freeswitch/ /etc/freeswitch/  
  
# Post install configuration.  
ADD sysv/init /etc/init.d/freeswitch  
RUN chmod +x /etc/init.d/freeswitch  
RUN update-rc.d -f freeswitch defaults  
ADD sysv/default /etc/default/freeswitch  
  
# Add the freeswitch user.  
RUN adduser --gecos "FreeSWITCH Voice Platform" \--no-create-home --disabled-
login --disabled-password --system --ingroup daemon --home
/usr/local/freeswitch freeswitch  
RUN chown -R freeswitch:daemon /usr/local/freeswitch  
  
# Create the log file.  
RUN mkdir /var/log/freeswitch/  
RUN touch /var/log/freeswitch/freeswitch.log  
RUN rm -rf /usr/local/freeswitch/log  
RUN ln -s /var/log/freeswitch/ /usr/local/freeswitch/log  
RUN chown -R freeswitch:daemon /var/log/freeswitch  
RUN chown -R freeswitch:daemon /usr/local/freeswitch  
  
# Link config files  
RUN rm -rf /usr/local/freeswitch/conf  
RUN ln -s /etc/freeswitch/ /usr/local/freeswitch/conf  
RUN chown -R freeswitch:daemon /etc/freeswitch/  
RUN chown -R freeswitch:daemon /usr/local/freeswitch  
  
# Update bin path  
ENV PATH=$PATH:/usr/local/freeswitch/bin/  
  
# Open the container up to the world.  
# sip port (to be used with kamailio)  
EXPOSE 11000  
# event_socket port  
EXPOSE 8021  
# kazoo port  
EXPOSE 8031  
EXPOSE 4369  
# Start the container.  
CMD service snmpd start && epmd -daemon && service freeswitch start && tail -f
/var/log/freeswitch/freeswitch.log  

