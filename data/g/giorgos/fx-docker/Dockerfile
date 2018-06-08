FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git curl moreutils gettext-base
bzip2 ca-certificates \  
libxt6 libgtk2.0-0 libdbus-glib-1-2 libasound2 libXcomposite1 libXdamage1
libXext6 libXrender1 libfontconfig libfreetype6 libgtk-3-0 libx11-xcb1 && \  
rm -rf /var/lib/apt  
  
ENV VERSION 59.0  
RUN curl
https://archive.mozilla.org/pub/mozilla.org/firefox/releases/$VERSION/linux-x86_64/en-
US/firefox-$VERSION.tar.bz2 | tar jx  
  
COPY Profile/.mozilla /root/.mozilla  
COPY bootstrap.sh /  
  
WORKDIR /firefox  
CMD ["/bootstrap.sh"]  

