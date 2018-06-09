FROM buildpack-deps:jessie-curl  
  
ENV WERCKER_VERSION 1.0.134  
ENV WERCKER_DOWNLOAD_URL
https://s3.amazonaws.com/downloads.wercker.com/cli/stable/linux_amd64/wercker  
ENV WERCKER_DOWNLOAD_SHA2
d769633a5acd1bf630130388169f6e0f08698cbf2ae058bd12e2ef28c295449c  
  
RUN curl ${WERCKER_DOWNLOAD_URL} -o /usr/local/bin/wercker \  
&& echo "${WERCKER_DOWNLOAD_SHA2} /usr/local/bin/wercker" | sha256sum -c - \  
&& chmod +x /usr/local/bin/wercker  

