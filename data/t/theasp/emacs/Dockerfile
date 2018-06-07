FROM theasp/userlayer:ubuntu16.04  
ARG http_proxy  
MAINTAINER Andrew Phillips <theasp@gmail.com>  
RUN set -ex; \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
873503A090750CDAEB0754D93FF0E01EEAAFC9CD; \  
echo deb http://ppa.launchpad.net/kelleyk/emacs/ubuntu xenial main >>
/etc/apt/sources.list; \  
apt-get update -q; \  
apt-get install -q -y \  
emacs25 \  
fonts-dejavu-extra \  
fonts-droid-fallback \  
fonts-fantasque-sans \  
fonts-font-awesome \  
fonts-freefont-ttf \  
fonts-hack-otf \  
fonts-jsmath \  
fonts-jura \  
fonts-liberation \  
fonts-lmodern \  
fonts-lyx \  
fonts-materialdesignicons-webfont \  
fonts-mathjax-extras \  
fonts-noto \  
fonts-opendyslexic \  
fonts-opensymbol \  
fonts-powerline \  
fonts-roboto \  
fonts-symbola \  
git \  
gnupg2 \  
hunspell \  
hunspell-en-ca \  
hunspell-en-us \  
littler \  
openjdk-8-jdk \  
r-recommended \  
subversion \  
supervisor \  
ttf-anonymous-pro \  
ttf-bitstream-vera \  
ttf-ubuntu-font-family \  
ttf-unifont \  
ttf-xfree86-nonfree \  
w3m  
COPY app/ /app/  

