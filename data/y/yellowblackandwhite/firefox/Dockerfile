FROM selenium/node-firefox-debug:2.47.1  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
#=======  
# Flash  
#=======  
ADD
https://fpdownload.adobe.com/get/flashplayer/pdc/24.0.0.186/flash_player_npapi_linux.x86_64.tar.gz
/tmp/  
RUN mkdir /tmp/install_flash_player_11_linux && \  
mkdir /usr/lib/flash-plugin/ && \  
mkdir -p /usr/lib/flash-plugin/ && \  
mkdir -p /usr/lib/firefox/browser/plugins/ && \  
tar -zxvf /tmp/flash_player_npapi_linux.x86_64.tar.gz -C
/tmp/install_flash_player_11_linux && \  
cd /tmp/install_flash_player_11_linux && \  
cp -r usr/* /usr && \  
cp libflashplayer.so /usr/lib/flash-plugin/ && \  
cp libflashplayer.so /usr/lib/firefox/browser/plugins/ && \  
chmod 775 /usr/lib/flash-plugin/libflashplayer.so && \  
chmod 775 /usr/lib/firefox/browser/plugins/libflashplayer.so && \  
rm -rf /tmp/install_flash_player_11_linux  
  
# #==============================  
# # Firefox Addons  
# #==============================  
# ADD install-mozilla-addon.sh /usr/local/sbin/install-mozilla-addon  
# RUN chmod +x /usr/local/sbin/install-mozilla-addon && \  
# install-mozilla-addon
https://addons.mozilla.org/firefox/downloads/latest/similarweb-sites-
recommendatio/addon-10548-latest.xpi?src=dp-btn-primary && \  
# install-mozilla-addon
https://addons.mozilla.org/firefox/downloads/latest/seo-status-pagerankalexa-
toolb/addon-56804-latest.xpi?src=dp-btn-primary  

