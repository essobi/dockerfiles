FROM debian:jessie  
  
ENV SPLUNK_PRODUCT splunk  
ENV SPLUNK_VERSION 6.6.2  
ENV SPLUNK_BUILD 4b804538c686  
ENV SPLUNK_FILENAME splunk-${SPLUNK_VERSION}-${SPLUNK_BUILD}-Linux-x86_64.tgz  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
ADD
https://download.splunk.com/products/${SPLUNK_PRODUCT}/releases/${SPLUNK_VERSION}/linux/${SPLUNK_FILENAME}
/tmp/${SPLUNK_FILENAME}  
ADD
https://download.splunk.com/products/${SPLUNK_PRODUCT}/releases/${SPLUNK_VERSION}/linux/${SPLUNK_FILENAME}.md5
/tmp/${SPLUNK_FILENAME}.md5  
  
# install the bits we need to get going.  
RUN apt-get update && apt-get install -y locales libgssapi-krb5-2 sudo git vim
\  
  
# make the "en_US.UTF-8" locale so splunk will be utf-8 enabled by default,
pdfgen dependency  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
  
# Get image ready for next phase  
&& (cd /tmp && md5sum -c ${SPLUNK_FILENAME}.md5) \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG en_US.utf8  

