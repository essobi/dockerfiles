FROM debian:jessie  
  
#################  
# utils  
#################  
  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
dnsutils \  
netcat \  
supervisor \  
sudo \  
tcpdump \  
unzip \  
wget \  
net-tools \  
locales \  
curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#################  
# Freeswitch  
#################  
  
RUN curl
https://files.freeswitch.org/repo/deb/debian/freeswitch_archive_g0.pub | apt-
key add \- && \  
echo "deb http://files.freeswitch.org/repo/deb/freeswitch-1.6/ jessie main" >
/etc/apt/sources.list.d/freeswitch.list && \  
apt-get update && \  
apt-get install -y \--force-yes \  
freeswitch-video-deps-most \  
libvorbis0a \  
libogg0 \  
libogg-dev \  
libvorbis-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git config --global pull.rebase true && \  
git clone https://freeswitch.org/stash/scm/fs/freeswitch.git freeswitch.git &&
\  
cd freeswitch.git  
  
RUN cd freeswitch.git && \  
./bootstrap.sh -j && \  
./configure --enable-core-pgsql-support && \  
perl -i -pe 's/applications\/mod_fsv/#applications\/mod_fsv/g' modules.conf &&
\  
perl -i -pe 's/codecs\/mod_vpx/#codecs\/mod_vpx/g' modules.conf && \  
perl -i -pe 's/codecs\/mod_g729/#codecs\/mod_g729/g' modules.conf && \  
perl -i -pe 's/codecs\/mod_g723_1/#codecs\/mod_g723_1/g' modules.conf && \  
perl -i -pe 's/codecs\/mod_ilbc/#codecs\/mod_ilbc/g' modules.conf && \  
perl -i -pe
's/#event_handlers\/mod_cdr_mongodb/event_handlers\/mod_cdr_mongodb/g'
modules.conf && \  
perl -i -pe
's/#event_handlers\/mod_cdr_pg_csv/event_handlers\/mod_cdr_pg_csv/g'
modules.conf && \  
perl -i -pe
's/#event_handlers\/mod_format_cdr/event_handlers\/mod_format_cdr/g'
modules.conf && \  
perl -i -pe 's/#event_handlers\/mod_json_cdr/event_handlers\/mod_json_cdr/g'
modules.conf && \  
perl -i -pe 's/#event_handlers\/mod_odbc_cdr/event_handlers\/mod_odbc_cdr/g'
modules.conf && \  
perl -i -pe 's/#applications\/mod_avmd/applications\/mod_avmd/g' modules.conf
&& \  
perl -i -pe 's/#applications\/mod_curl/applications\/mod_curl/g' modules.conf
&& \  
perl -i -pe 's/#applications\/mod_mongo/applications\/mod_mongo/g'
modules.conf && \  
perl -i -pe 's/#applications\/mod_redis/applications\/mod_redis/g'
modules.conf && \  
perl -i -pe 's/#applications\/mod_distributor/applications\/mod_distributor/g'
modules.conf && \  
perl -i -pe 's/#applications\/mod_easyroute/applications\/mod_easyroute/g'
modules.conf && \  
perl -i -pe 's/#applications\/mod_spy/applications\/mod_spy/g' modules.conf &&
\  
perl -i -pe 's/#applications\/mod_say_pt/applications\/mod_say_pt/g'
modules.conf && \  
perl -i -pe 's/#applications\/mod_callcenter/applications\/mod_callcenter/g'
modules.conf && \  
perl -i -pe 's/#formats\/mod_shout/formats\/mod_shout/g' modules.conf && \  
make && \  
make install && \  
make samples && \  
cd /  
  
#################  
# freeswitch cfg  
#################  
  
RUN mkdir /var/log/freeswitch  
RUN mkdir /var/lib/freeswitch  
  
ENV PATH="/usr/local/freeswitch/bin:${PATH}"  
  
#################  
# volumes  
#################  
  
VOLUME ["/etc/freeswitch"]  
  
VOLUME ["/etc/freeswitch/generated"]  
  
#################  
# ports  
#################  
  
# SIP port  
EXPOSE 5060/udp  
EXPOSE 5060/tcp  
  
# XML RPC  
EXPOSE 8080/tcp  
  
#################  
# entry point  
#################  
  
CMD ["/usr/local/freeswitch/bin/freeswitch -conf /etc/freeswitch -log
/var/log/freeswitch/log -db /var/lib/freeswitch"]  

