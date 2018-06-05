FROM ruby:latest  
  
ENV TRANSACTD_VERSION 3.7.2  
ENV TRANSACTD_GEM_MD5 cb75679f9fa2ebe0cf0f885f20bf0c00  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y wget \  
&& wget -O transactd-${TRANSACTD_VERSION}.gem
"http://www.bizstation.jp/al/transactd/download/docker/transactd-${TRANSACTD_VERSION}.gem.zip"
\  
&& echo "${TRANSACTD_GEM_MD5} transactd-${TRANSACTD_VERSION}.gem" | md5sum -c
- \  
&& gem install transactd-${TRANSACTD_VERSION}.gem \  
&& rm -f transactd-${TRANSACTD_VERSION}.gem \  
&& apt-get purge -y --auto-remove wget \  
&& rm -rf /var/lib/apt/lists/*  

