FROM mouyigang/aspconnect  
MAINTAINER Andy Mou <mouyigang@gmail.com>  
USER root  
  
RUN sed -i.bak 's/sid main/sid main contrib/g' /etc/apt/sources.list && \  
apt-get update && apt-get install -y \  
bzip2 \  
ca-certificates \  
wget \  
curl \  
libdbus-glib-1-2 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
#============================================  
# Google Chrome  
#============================================  
# can specify versions by CHROME_VERSION;  
# e.g. google-chrome-stable=53.0.2785.101-1  
# google-chrome-beta=53.0.2785.92-1  
# google-chrome-unstable=54.0.2840.14-1  
# latest (equivalent to google-chrome-stable)  
# google-chrome-beta (pull latest beta)  
#============================================  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN apt-get update -qqy && apt-get install -y net-tools && rm -rf
/var/lib/apt/lists/* /var/cache/apt/*  
#=========  
# Firefox  
#=========  
ARG FIREFOX_VERSION=45.8.0esr  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
  
COPY local.conf /etc/fonts/local.conf  
  
#ENTRYPOINT [ "/usr/bin/firefox" ]  

