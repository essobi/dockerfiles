FROM debian:jessie  
  
COPY mod_odbc_query /usr/src/mod_odbc_query  
COPY mod_odbc_query.patch /usr/src/  
  
RUN apt-get update -y && apt-get install -y wget cron unixodbc unixodbc-dev
libmyodbc msmtp  
  
RUN echo "deb http://files.freeswitch.org/repo/deb/freeswitch-1.4/ jessie
main" > /etc/apt/sources.list.d/freeswitch.list \  
&& wget -O - http://files.freeswitch.org/repo/deb/freeswitch-1.4/key.gpg |apt-
key add -  
  
RUN apt-get update -y \  
&& apt-get install -y --force-yes freeswitch-video-deps-most  
  
WORKDIR /usr/src  
  
RUN git clone https://freeswitch.org/stash/scm/fs/freeswitch.git \  
&& cd freeswitch \  
&& git checkout v1.4.26 \  
&& mv ../mod_odbc_query src/mod/applications/ \  
&& patch -p1 < ../mod_odbc_query.patch \  
&& ./bootstrap.sh -j \  
&& ./configure \  
&& sed -i '/mod_erlang_event/s/#//g' modules.conf \  
&& sed -i '/mod_flite/s/#//g' modules.conf \  
&& echo 'applications/mod_odbc_query' >> modules.conf \  
&& make \  
&& make install \  
&& make hd-sounds-install hd-moh-install hd-sounds-fr-install \  
&& rm -rf freeswitch \  
&& apt-get -y clean  
  
ADD odbcinst.ini /etc/  
#COPY freeswitch_conf /usr/local/freeswitch/conf  
#COPY ivr /usr/local/freeswitch/sounds/ivr  
VOLUME /usr/local/freeswitch/log /usr/local/freeswitch/db  
  
ADD start.sh /usr/local/freeswitch/  
WORKDIR /usr/local/freeswitch  
  
ADD crontab /etc/cron.d/  
RUN chmod +x /etc/cron.d/crontab  
  
ENV
PATH=/usr/local/freeswitch/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
CMD ["./start.sh"]  

