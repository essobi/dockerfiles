FROM ubuntu:14.04  
MAINTAINER Sébastien Brice <fulc927@gmail.com>  
ENV build_date 2015-04-23  
RUN apt-get update  
RUN apt-get install libmysqlclient-dev make g++ curl vim ksh unixodbc-dev
ngrep libmyodbc gcc libstdc++6 libstdc++-4.8-dev cpp libncurses5
libncurses5-dev libxml2 libxml2-dev sqlite libsqlite3-dev openssl libnewt0.52
libuuid1 uuid-dev uuid-runtime tar wireshark-common tshark -y  
  
WORKDIR /  
  
ENV AUTOBUILD_UNIXTIME 123123  
# Download asterisk.  
# This is an experiment for Asterisk 13  
RUN curl -sf -o /tmp/asterisk.tar.gz -L
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz  
  
# gunzip asterisk  
RUN mkdir /tmp/asterisk  
RUN tar -xzf /tmp/asterisk.tar.gz -C /tmp/asterisk --strip-components=1  
WORKDIR /tmp/asterisk  
  
# Extra deps.  
RUN apt-get install libjansson-dev -y  
  
# make asterisk.  
ENV rebuild_date 2016-04-23  
# Configure  
RUN ./configure --libdir=/usr/lib64 --disable-asteriskssl 1> /dev/null  
# Remove the native build option  
RUN make menuselect.makeopts  
# Idea!  
# menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts  
#RUN menuselect/menuselect --enable ODBC_STORAGE menuselect.makeopts  
RUN echo "MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE" >> menuselect.makeopts  
# from:
https://wiki.asterisk.org/wiki/display/AST/Building+and+Installing+Asterisk  
RUN sed -i "s/BUILD_NATIVE//" menuselect.makeopts  
# Continue with a standard make.  
RUN make 1> /dev/null  
RUN make install 1> /dev/null  
RUN make samples 1> /dev/null  
WORKDIR /  
# clean up after compil  
RUN rm -rf /tmp/asterisk  
  
# Update max number of open files.  
RUN sed -i -e 's/# MAXFILES=/MAXFILES=/' /usr/sbin/safe_asterisk  
RUN sed -i -e 's/enabled = yes/enabled = no /' /etc/asterisk/ari.conf  
RUN mkdir -p /etc/asterisk  
# ADD modules.conf /etc/asterisk/  
RUN touch /etc/asterisk/extensions.conf  
RUN touch /etc/asterisk/sip.conf  
RUN mkdir /sysadm  
RUN mkdir /sysadm/tmp  
COPY sys_FCT_SYS_network.sh /sysadm  
COPY sys_env.sh /sysadm  
# Set environment variables.  
ADD .profile /root/.bashrc  
ADD .profile /root/.kshrc  
ADD .odbc.ini /etc/odbc.ini  
ADD .odbcinst.ini /etc/odbcinst.ini  
ADD extconfig.conf /etc/asterisk/extconfig.conf  
ADD res_odbc.conf /etc/asterisk/res_odbc.conf  
# tweak open port on asterisk (only :5080 needed)  
RUN echo "noload => chan_skinny.so" >> /etc/asterisk/modules.conf  
RUN echo "noload => chan_mgcp.so" >> /etc/asterisk/modules.conf  
RUN echo "noload => pbx_dundi.so" >> /etc/asterisk/modules.conf  
RUN echo "noload => iax.so" >> /etc/asterisk/modules.conf  
RUN echo "noload => chan_iax2.so" >> /etc/asterisk/modules.conf  
RUN echo "noload => chan_unistim.so" >> /etc/asterisk/modules.conf  
ENV HOME /root  
# Define working directory.  
WORKDIR /root  
  
CMD asterisk -f  

