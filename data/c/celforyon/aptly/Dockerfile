FROM debian:jessie  
MAINTAINER Alexis Pereda <alexis@pereda.fr>  
  
LABEL maintainer="Alexis Pereda <alexis@pereda.fr>"  
LABEL version="1.0"  
LABEL description="Debian package publisher (using aptly)"  
  
RUN echo >/etc/apt/sources.list.d/stretch.list 'deb
http://httpredir.debian.org/debian stretch main'  
COPY etc/apt/preferences /etc/apt/preferences  
  
RUN apt update \  
&& apt install --no-install-recommends --no-install-suggests -y --force-yes
inotify-tools gnupg=1.4.18-7+deb8u3 \  
&& apt install --no-install-recommends --no-install-suggests -y --force-yes
-tstretch aptly \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY etc/aptly.conf /etc/aptly.conf  
COPY bin /usr/local/bin  
  
WORKDIR /opt/aptly  
  
VOLUME ["/opt/aptly"]  
VOLUME ["/shared"]  
  
ENTRYPOINT ["start"]  

