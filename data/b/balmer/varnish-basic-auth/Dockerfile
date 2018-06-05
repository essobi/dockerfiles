FROM phusion/baseimage:0.9.18  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV VARNISHD_PARAMS -a :80 -p default_ttl=3600 -p default_grace=3600  
CMD ["/sbin/my_init"]  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt-get install -y apt-transport-https \  
&& apt-get install -y git-core zlib1g-dev automake build-essential libtool
libssl-dev \  
libreadline-dev libyaml-dev libsqlite3-dev ncurses-dev sqlite3 libxml2-dev
libxslt1-dev \  
libpcre3-dev libcurl4-openssl-dev python-docutils python-software-properties
libvarnishapi-dev  
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -  
RUN printf "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.1
\ndeb-src https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list && apt-get update  
RUN apt-get install -qy varnish  
RUN apt-get source varnish && rm *.diff.gz *.dsc *.tar.gz \  
&& mv varnish* varnish-source && cd varnish-source && ./autogen.sh &&
./configure --prefix=/usr/sbin && make  
RUN git clone http://git.gnu.org.ua/cgit/vmod-basicauth.git && cd vmod-
basicauth \  
&& git clone http://git.gnu.org.ua/repo/acvmod.git && ./bootstrap \  
&& ./configure VARNISHSRC=/varnish-source VMODDIR=/usr/lib/varnish/vmods/ &&
make && make install && make check  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
EXPOSE 80  
RUN mkdir /etc/service/varnish  
ADD start.sh /etc/service/varnish/run  
ADD config/default.vcl /etc/varnish/default.vcl  
ADD config/htpasswd /etc/varnish/htpasswd  
RUN chmod +x /etc/service/varnish/run

