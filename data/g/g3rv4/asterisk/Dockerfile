FROM ubuntu:14.04  
MAINTAINER Gervasio Marchand <gmc@gmc.uy>  
ENV build_date 2016-07-28  
  
WORKDIR /tmp  
RUN apt-get update && \  
apt-get install -y build-essential git-core pkg-config subversion libjansson-
dev sqlite autoconf \  
automake libtool libxml2-dev libncurses5-dev unixodbc unixodbc-dev
libasound2-dev libogg-dev \  
libvorbis-dev libneon27-dev libspandsp-dev libmyodbc uuid uuid-dev sqlite3
libsqlite3-dev \  
libgnutls-dev wget && \  
  
wget
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz
&& \  
tar -xzf asterisk-13-current.tar.gz && \  
rm asterisk-13-current.tar.gz && \  
cd asterisk-* && \  
./configure && \  
contrib/scripts/get_mp3_source.sh && \  
make menuselect.makeopts && \  
menuselect/menuselect \  
  
# required for asterisk to work ok in docker (check
http://stackoverflow.com/a/19610145/920295)  
--disable BUILD_NATIVE \  
  
# MENUSELECT_ADDONS category  
--disable chan_mobile \  
--enable format_mp3 \  
--disable res_config_mysql \  
--disable app_mysql \  
--disable cdr_mysql \  
  
# MENUSELECT_APPS category  
--disable app_db \  
  
# MENUSELECT_CHANNELS category  
--disable-category MENUSELECT_CHANNELS \  
--enable chan_sip \  
  
# MENUSELECT_RES category (I do not want pjsip)  
--disable res_pjproject \  
--disable res_pjsip \  
--disable res_pjsip_acl \  
--disable res_pjsip_authenticator_digest \  
--disable res_pjsip_caller_id \  
--disable res_pjsip_config_wizard \  
--disable res_pjsip_dialog_info_body_generator \  
--disable res_pjsip_diversion \  
--disable res_pjsip_dlg_options \  
--disable res_pjsip_dtmf_info \  
--disable res_pjsip_endpoint_identifier_anonymous \  
--disable res_pjsip_endpoint_identifier_ip \  
--disable res_pjsip_endpoint_identifier_user \  
--disable res_pjsip_exten_state \  
--disable res_pjsip_header_funcs \  
--disable res_pjsip_logger \  
--disable res_pjsip_messaging \  
--disable res_pjsip_multihomed \  
--disable res_pjsip_mwi \  
--disable res_pjsip_mwi_body_generator \  
--disable res_pjsip_nat \  
--disable res_pjsip_notify \  
--disable res_pjsip_one_touch_record_info \  
--disable res_pjsip_outbound_authenticator_digest \  
--disable res_pjsip_outbound_publish \  
--disable res_pjsip_outbound_registration \  
--disable res_pjsip_path \  
--disable res_pjsip_pidf_body_generator \  
--disable res_pjsip_pidf_digium_body_supplement \  
--disable res_pjsip_pidf_eyebeam_body_supplement \  
--disable res_pjsip_publish_asterisk \  
--disable res_pjsip_pubsub \  
--disable res_pjsip_refer \  
--disable res_pjsip_registrar \  
--disable res_pjsip_registrar_expire \  
--disable res_pjsip_rfc3326 \  
--disable res_pjsip_sdp_rtp \  
--disable res_pjsip_send_to_voicemail \  
--disable res_pjsip_session \  
--disable res_pjsip_sips_contact \  
--disable res_pjsip_t38 \  
--disable res_pjsip_transport_management \  
--disable res_pjsip_transport_websocket \  
--disable res_pjsip_xpidf_body_generator \  
  
--disable-category MENUSELECT_TESTS \  
  
menuselect.makeopts && \  
make && \  
make install && \  
  
# The conf files will be populated by the init.sh script  
# make samples && \  
  
cd /tmp && \  
rm -rf asterisk-* && \  
sed -i -e 's/# MAXFILES=/MAXFILES=/' /usr/sbin/safe_asterisk && \  
  
# uninstall wget so that it's not in the image  
apt-get remove -y wget && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/default-conf.tgz files/init.sh /tmp/  
  
VOLUME ["/etc/asterisk", "/var/spool/asterisk", "/var/log/asterisk"]  
  
CMD ["/bin/bash", "/tmp/init.sh"]  

