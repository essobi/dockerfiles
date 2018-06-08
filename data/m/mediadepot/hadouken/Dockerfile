FROM mediadepot/base  
# Install apk packages  
RUN apk --no-cache --update add openssl-dev bash unzip wget  
  
#Create hadouken folder structure & set as volumes  
RUN mkdir -p /srv/hadouken/app && \  
mkdir -p /srv/hadouken/data && \  
mkdir -p /srv/hadouken/config  
  
WORKDIR /srv/hadouken/app  
  
#Download Hadouken source  
RUN apk --no-cache --update add perl && \  
git clone https://github.com/hadouken/hadouken.git /srv/hadouken/app && \  
cd /srv/hadouken/app && \  
git checkout tags/v5.2.0 && \  
git submodule update --init && \  
apk del perl  
  
#Copy over modified build scripts.  
ADD ./linux_build.sh /srv/hadouken/app/linux/build.sh  
ADD ./linux_install-boost.sh /srv/hadouken/app/linux/install-boost.sh  
#ADD ./linux_install-libtorrent.sh /srv/hadouken/app/linux/install-
libtorrent.sh  
RUN chmod u+x /srv/hadouken/app/linux/build.sh  
RUN chmod u+x /srv/hadouken/app/linux/install-boost.sh  
#RUN chmod u+x /srv/hadouken/app/linux/install-libtorrent.sh  
#Install Build dependenices, build boost, libtorrent and hadouken then remove
build deps (in one step)  
RUN apk --no-cache --update add --virtual build-dependencies cmake perl
autoconf automake build-base zip libtool linux-headers && \  
./linux/install-boost.sh && \  
./linux/install-libtorrent.sh  
RUN ./linux/build.sh  
  
#Copy over start script and docker-gen files  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
  
VOLUME ["/srv/hadouken/app", "/srv/hadouken/config", "/srv/hadouken/data"]  
  
EXPOSE 8080  
#CMD ["/srv/start.sh"]  
CMD ["sh"]

