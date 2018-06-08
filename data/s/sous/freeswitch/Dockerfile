FROM ubuntu:12.04  
MAINTAINER sous "gitsous@gmail.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq update  
RUN apt-get install -y --no-install-recommends build-essential autoconf
automake libtool zlib1g-dev libjpeg-dev libncurses-dev libssl-dev
libcurl4-openssl-dev python-dev libexpat1-dev libtiff-dev libx11-dev wget git
libav-tools libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev
libavutil-dev libavbin-dev libavcodec-extra-53 libavdevice-extra-53
libavfilter-extra-2 libavformat-extra-53 libsofia-sip-ua-dev libvpx-dev
libfreetype6-dev libjpeg-turbo8-dev erlang-dev uuid-dev libgdbm-dev ladspa-sdk
libflac-dev libvlc-dev default-jdk gcj-jdk libyaml-dev automake autoconf
libtool dpkg-dev libc6-dev pkg-config libssl-dev unixodbc-dev libpq-dev
libjpeg8-dev python-dev erlang-dev doxygen uuid-dev libexpat1-dev libgdbm-dev
libdb-dev bison zlib1g-dev ladspa-sdk libogg-dev libasound2-dev libasound2-dev
libx11-dev libpq-dev erlang-dev libsnmp-dev libflac-dev libogg-dev libvorbis-
dev libvlc-dev default-jdk gcj-jdk libperl-dev python-dev libyaml-dev
libsqlite3-dev build-essential libpcre3-dev libspeex-dev libspeexdsp-dev
libldns-dev libedit-dev libpq-dev libmemcached-dev &&\  
ln -s /usr/include/postgresql/libpq-fe.h /usr/include/ &&\  
ln -s /usr/include/postgresql/postgres_ext.h /usr/include/ &&\  
git clone -b master git://git.freeswitch.org/freeswitch
/usr/local/src/freeswitch &&\  
cd /usr/local/src/freeswitch &&\  
./bootstrap.sh -j &&\  
for module in applications/mod_abstraction applications/mod_avmd
applications/mod_blacklist applications/mod_callcenter
applications/mod_cidlookup applications/mod_cluechoo applications/mod_commands
applications/mod_conference applications/mod_curl applications/mod_db
applications/mod_directory applications/mod_distributor
applications/mod_dptools applications/mod_easyroute applications/mod_enum
applications/mod_esf applications/mod_esl applications/mod_expr
applications/mod_fifo applications/mod_fsk applications/mod_fsv
applications/mod_hash applications/mod_httapi applications/mod_http_cache
applications/mod_ladspa applications/mod_lcr applications/mod_memcache
applications/mod_nibblebill applications/mod_oreka applications/mod_random
applications/mod_redis applications/mod_rss applications/mod_sms
applications/mod_snapshot applications/mod_snipe_hunt applications/mod_snom
applications/mod_sonar applications/mod_soundtouch applications/mod_spandsp
applications/mod_spy applications/mod_stress applications/mod_translate
applications/mod_valet_parking applications/mod_vmd applications/mod_voicemail
applications/mod_voicemail_ivr asr_tts/mod_flite asr_tts/mod_pocketsphinx
asr_tts/mod_tts_commandline asr_tts/mod_unimrcp codecs/mod_amr
codecs/mod_amrwb codecs/mod_b64 codecs/mod_bv codecs/mod_celt
codecs/mod_codec2 codecs/mod_dahdi_codec codecs/mod_g723_1 codecs/mod_g729
codecs/mod_h26x codecs/mod_isac codecs/mod_mp4v codecs/mod_opus
codecs/mod_silk codecs/mod_speex codecs/mod_theora codecs/mod_vp8
dialplans/mod_dialplan_asterisk dialplans/mod_dialplan_directory
dialplans/mod_dialplan_xml directories/mod_ldap endpoints/mod_alsa
endpoints/mod_dingaling endpoints/mod_html5 endpoints/mod_loopback
endpoints/mod_portaudio endpoints/mod_rtmp endpoints/mod_skinny
endpoints/mod_skypopen endpoints/mod_sofia event_handlers/mod_cdr_csv
event_handlers/mod_cdr_mongodb event_handlers/mod_cdr_pg_csv
event_handlers/mod_cdr_sqlite event_handlers/mod_erlang_event
event_handlers/mod_event_multicast event_handlers/mod_event_socket
event_handlers/mod_event_test event_handlers/mod_event_zmq
event_handlers/mod_json_cdr event_handlers/mod_radius_cdr
event_handlers/mod_rayo event_handlers/mod_snmp formats/mod_local_stream
formats/mod_native_file formats/mod_portaudio_stream formats/mod_shell_stream
formats/mod_sndfile formats/mod_ssml formats/mod_tone_stream formats/mod_vlc
languages/mod_java languages/mod_lua languages/mod_perl languages/mod_python
languages/mod_yaml loggers/mod_console loggers/mod_logfile loggers/mod_syslog
say/mod_say_de say/mod_say_en say/mod_say_es say/mod_say_fa say/mod_say_fr
say/mod_say_he say/mod_say_hr say/mod_say_hu say/mod_say_it say/mod_say_ja
say/mod_say_nl say/mod_say_pl say/mod_say_pt say/mod_say_ru say/mod_say_th
say/mod_say_zh timers/mod_posix_timer timers/mod_timerfd xml_int/mod_xml_cdr
xml_int/mod_xml_curl xml_int/mod_xml_rpc xml_int/mod_xml_scgi; do if ! grep -e
"^$module" ; then echo $module >> /usr/local/src/freeswitch/modules.conf ; fi;
done &&\  
./configure --prefix=/opt/freeswitch &&\  
make; make install && make all cd-sounds-install cd-moh-install && apt-get
clean &&\  
rm -fr /usr/local/src/freeswitch &&\  
dpkg --purge build-essential autoconf automake libtool zlib1g-dev libjpeg-dev
libncurses5-dev libssl-dev libcurl4-openssl-dev python-dev libexpat1-dev
libtiff4-dev libx11-dev libavcodec-dev libavdevice-dev libavfilter-dev
libavformat-dev libavutil-dev libavbin-dev libsofia-sip-ua-dev libvpx-dev
libfreetype6-dev libjpeg-turbo8-dev erlang-dev uuid-dev libgdbm-dev ladspa-sdk
libflac-dev libvlc-dev gcj-jdk libyaml-dev pkg-config libssl-dev unixodbc-dev
libpq-dev libjpeg8-dev python-dev erlang-dev doxygen uuid-dev libexpat1-dev
libgdbm-dev libdb-dev bison zlib1g-dev libogg-dev libasound2-dev
libasound2-dev libx11-dev libpq-dev erlang-dev libsnmp-dev libflac-dev libogg-
dev libvorbis-dev libvlc-dev default-jdk libperl-dev python-dev libyaml-dev
libsqlite3-dev libpcre3-dev libspeex-dev libspeexdsp-dev libldns-dev libedit-
dev libpq-dev libmemcached-dev python2.7-dev libgnutls-dev zlib1g-dev
libidn11-dev libvlccore-dev cj-4.6-jdk comerr-dev libgcrypt11-dev libgcj12-dev
zlib1g-dev gcj-4.6-jdk librtmp-dev krb5-multidev libgnutls-dev libkrb5-dev  
  
VOLUME ["/opt/freeswitch/conf"]  
EXPOSE 8021  
CMD ["/opt/freeswitch/bin/freeswitch","-c"]  

