FROM httpd:2.4.20  
MAINTAINER Ovidiu-Florin Bogdan (ovidiu.b13@gmail.com)  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV REVIEWBOARD_VERSION 2.5.6.1  
ENV MOD_WSGI_VERSION 4.5.3  
RUN apt update && apt install -y \  
patch \  
subversion \  
memcached \  
ca-certificates  
RUN apt update && apt install -y \  
python-setuptools \  
python-dev \  
python-mysqldb \  
python-svn  
RUN apt update && apt install -y \  
libjpeg-dev \  
zlib1g-dev \  
libffi-dev \  
libssl-dev  
  
RUN easy_install -U setuptools  
RUN easy_install pip  
RUN pip install python-memcached  
RUN pip install mysql-python  
  
RUN apt-get install gcc make wget -s | grep "Inst " | cut -f 2 -d " " > gcc-
deps.txt  
RUN apt install -y gcc make wget  
  
RUN pip install ReviewBoard==$REVIEWBOARD_VERSION  
  
RUN wget
https://github.com/GrahamDumpleton/mod_wsgi/archive/$MOD_WSGI_VERSION.tar.gz \  
-O mod_wsgi-$MOD_WSGI_VERSION.tar.gz \  
&& tar xzvf mod_wsgi-$MOD_WSGI_VERSION.tar.gz \  
&& rm mod_wsgi-$MOD_WSGI_VERSION.tar.gz \  
&& cd mod_wsgi-$MOD_WSGI_VERSION \  
&& ./configure \  
&& make \  
&& make install \  
&& cd ../ \  
&& rm -rf mod_wsgi-$MOD_WSGI_VERSION  
  
RUN apt remove -y `cat gcc-deps.txt | tr "\n" " "` && rm gcc-deps.txt  
  
COPY entrypoint.sh /entrypoint.sh  
COPY httpd.conf /usr/local/apache2/conf/httpd.conf  
  
EXPOSE 80  
VOLUME /var/www/  
  
ENTRYPOINT ["/entrypoint.sh"]  

