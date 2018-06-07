# Dockerfile for the Redlink Search CI Envirnoment  
FROM debian:stretch  
  
MAINTAINER sergio.fernandez@redlink.co  
  
ADD . /src  
WORKDIR /src  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# prepare ci environment  
RUN apt-get update -qq \  
&& apt-get install -qq -y \  
locales \  
apt-utils \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
RUN apt-get update -qq \  
&& apt-get install -y \  
nodejs-legacy \  
npm \  
ruby-compass \  
ghostscript \  
imagemagick \  
openjdk-8-jdk \  
maven \  
mongodb  
RUN npm install -g grunt grunt-cli bower  
RUN echo '{ "allow_root": true }' > ~/.bowerrc  
  
# clean-up  
RUN apt-get update -qq \  
&& apt-get -y clean -qq \  
&& apt-get -y autoclean -qq \  
&& apt-get -y autoremove -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
# entrypoint  
RUN cp start.sh /usr/local/bin/redlink-search-env-start.sh  
ENTRYPOINT ["/usr/local/bin/redlink-search-env-start.sh"]  
  

