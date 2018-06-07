FROM dockercore/opensuse:12.3  
RUN (zypper -n in curl ca-certificates* &&\  
zypper -n in yum-utils &&\  
zypper ar -t YUM https://packages.docker.com/1.13/yum/repo/main/opensuse/12.3
docker-1.13 &&\  
rpm --import 'https://sks-
keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e')  
  
ENV DOWNLOAD_DIR /data  
  
CMD zypper -n --cache-dir=${DOWNLOAD_DIR} in \--download-only docker-engine &&
find /data -name "*.rpm" -exec cp {} /data \; && rm -rf /data/packages
/data/raw /data/solv  

