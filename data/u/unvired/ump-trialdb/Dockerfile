FROM ubuntu:14.04  
MAINTAINER Unvired <support@unvired.io>  
  
RUN apt-get update -yqq \  
&& apt-get install -y \--no-install-recommends curl wget ca-certificates \  
&& mkdir -p /var/unvired/UMP3/db \  
&& mkdir -p /var/unvired/common/pa/config \  
&& mkdir -p /var/unvired/common/pa/UNVIRED.APP482129901084 \  
&& mkdir -p /var/unvired/common/pa/Revision/UNVIRED.APP482129901084/1 \  
&& mkdir -p /var/unvired/common/unvired \  
&& mkdir -p /var/unvired/common/keystore/PK12_FILE_FOLDER/UNVIRED  
  
LABEL vendor="Unvired Inc." \  
com.unvired.UMP.module="DATA" \  
com.unvired.UMP.release="1.0.2" \  
com.unvired.UMP.release-date="18-Dec-2015"  
# The required files - UMP db, Quartz db, root company key, PA  
  
RUN wget -q -O/var/unvired/UMP3/db/ump-platform.h2.db
https://owncloud.unvired.com/index.php/s/63JdM1Ply0Zcscz/download  
RUN wget -q -O/var/unvired/UMP3/db/quartz.h2.db
https://owncloud.unvired.com/index.php/s/uKf2ltm6dzgn8sI/download  
RUN wget -q
-O/var/unvired/common/keystore/PK12_FILE_FOLDER/UNVIRED/UNVIRED_keystore.p12
https://owncloud.unvired.com/index.php/s/zfm7tKsfATszQCd/download  
RUN wget -q -O/var/unvired/common/pa/config/quartz.properties
https://owncloud.unvired.com/index.php/s/CFDCJpCyYCD5l3U/download  
RUN wget -q
-O/var/unvired/common/pa/Revision/UNVIRED.APP482129901084/1/UNVIRED_SAP_CUSTOMER_SEARCH.jar
https://owncloud.unvired.com/index.php/s/9HdPTQPFWs50Rzf/download  
RUN wget -q
-O/var/unvired/common/pa/UNVIRED.APP482129901084/UNVIRED_SAP_CUSTOMER_SEARCH.jar
https://owncloud.unvired.com/index.php/s/9HdPTQPFWs50Rzf/download  
  
# Create /var/unvired volume  
VOLUME /var/unvired

