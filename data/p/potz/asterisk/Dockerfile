FROM debian:wheezy  
MAINTAINER Potiguar Faga <potz@potz.me>  
  
RUN apt-get update && apt-get install -y \  
build-essential wget libsqlite3-dev libncurses5-dev \  
uuid-dev libjansson-dev libxml2-dev libssl-dev && \  
wget
http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-13.3.2.tar.gz
&& \  
tar zxf asterisk-13.3.2.tar.gz && cd asterisk-13.3.2 && \  
./configure && make menuselect && \  
menuselect/menuselect \  
--disable-category MENUSELECT_ADDONS \  
--disable-category MENUSELECT_APPS \  
--disable-category MENUSELECT_BRIDGES \  
--disable-category MENUSELECT_CDR \  
--disable-category MENUSELECT_CEL \  
--disable-category MENUSELECT_CHANNELS \  
--enable-category MENUSELECT_CODECS \  
--enable-category MENUSELECT_FORMATS \  
--disable-category MENUSELECT_FUNCS \  
--disable-category MENUSELECT_PBX \  
--disable-category MENUSELECT_RES \  
--disable-category MENUSELECT_TESTS \  
--disable-category MENUSELECT_OPTS_app_voicemail \  
--disable-category MENUSELECT_UTILS \  
--disable-category MENUSELECT_AGIS \  
--disable-category MENUSELECT_EMBED \  
--disable-category MENUSELECT_CORE_SOUNDS \  
--disable-category MENUSELECT_MOH \  
--disable-category MENUSELECT_EXTRA_SOUNDS \  
--enable app_controlplayback \  
--enable app_dial \  
--enable app_exec \  
--enable app_originate \  
--enable app_queue \  
--enable app_record \  
--enable app_senddtmf \  
--enable app_stasis \  
--enable app_verbose \  
--enable app_waituntil \  
--enable chan_sip \  
--enable pbx_config \  
--enable pbx_realtime \  
--enable res_agi \  
--enable res_ari \  
--enable res_ari_channels \  
--enable res_ari_events \  
--enable res_ari_playbacks \  
--enable res_ari_recordings \  
--enable res_ari_sounds \  
--enable res_ari_device_states \  
--enable res_realtime \  
--enable res_rtp_asterisk \  
--enable res_rtp_multicast \  
--enable res_stasis \  
--enable res_stasis_answer \  
--enable res_stasis_device_state \  
--enable res_stasis_playback \  
--enable res_stasis_recording \  
--enable res_stun_monitor \  
--enable res_timing_timerfd \  
--enable func_callcompletion \  
--enable func_callerid \  
--disable BUILD_NATIVE \  
menuselect.makeopts && \  
make config && make && make install && \  
mkdir -p /var/lib/asterisk/phoneprov/ && make samples && \  
make dist-clean && cd .. && \  
rm asterisk-13.3.2.tar.gz && rm -rf /asterisk/13-3.2 && \  
apt-get remove -y build-essential wget && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8088 5038 5060 5061 5060/udp 10000-20000/udp  
  
CMD ["/usr/sbin/asterisk", "-f"]  

