FROM alpine  
  
ENV RTM_VERSION 0.9.4-5  
ENV RTM_DOWNLOAD_URL "ftp://ftp.ovh.net/made-in-ovh/rtm/install_rtm-"  
ENV RTM_INSTALLER_CHECKSUM
16dcde3cf46f82dcacfb63535b9375c97f0cc1ba4e412c086f0f03dd8a5483ac  
ENV RTM_REPORT_INTERVAL 60  
RUN apk add --no-cache bash curl sed gawk bind-tools screen dmidecode pciutils
bzip2 perl procps coreutils bc  
  
COPY init.sh /usr/bin/init.sh  
  
VOLUME /cache  
  
CMD ["/usr/bin/init.sh"]  

