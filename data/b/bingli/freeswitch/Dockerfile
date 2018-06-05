FROM bingli/freeswitch:1.6_deps  
  
RUN apt-get update -y && apt-get install -y cron  
  
ADD erlang_outbound_reentry.patch /usr/src  
  
WORKDIR /usr/src/  
  
RUN git clone -b v1.6 --single-branch
https://freeswitch.org/stash/scm/fs/freeswitch.git freeswitch.git \  
&& cd freeswitch.git \  
&& git checkout v1.6.19 \  
&& patch -p1 < ../erlang_outbound_reentry.patch \  
&& ./bootstrap.sh -j \  
&& ./configure \  
&& sed -i '/mod_erlang_event/s/#//' modules.conf \  
&& sed -i '/mod_flite/s/#//' modules.conf \  
&& sed -i '/mod_ilbc/s/#//' modules.conf \  
&& sed -i '/mod_json_cdr/s/#//' modules.conf \  
&& sed -i '/mod_xml_curl/s/#//' modules.conf \  
&& sed -i '/mod_shout/s/#//' modules.conf \  
&& make \  
&& make install \  
&& make cd-sounds-install \  
&& make cd-moh-install \  
&& make samples \  
&& cd .. && rm -rf freeswitch.git  
  
ADD crontab /etc/cron.d/  
RUN chmod +x /etc/cron.d/crontab  
  
ENV PATH=/usr/local/freeswitch/bin:$PATH  
  
ADD odbcinst.ini /etc/  
RUN apt-get install -y msmtp libmyodbc unixodbc  
  
WORKDIR /usr/local/freeswitch  
  
CMD service cron start; sleep 5; freeswitch -hp -nonat -nc -reincarnate-reexec
&& sleep infinity  

