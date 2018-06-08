  
FROM centos:7  
MAINTAINER "fireweed-lin" hikelin314@gmail.com  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r httpd24 && useradd -r --create-home -g httpd24 httpd24  
  
ENV HTTPD_PREFIX /usr/local/apache2  
ENV PATH $HTTPD_PREFIX/bin:$PATH  
RUN mkdir -p "$HTTPD_PREFIX" \  
&& chown httpd24:httpd24 "$HTTPD_PREFIX"  
WORKDIR $HTTPD_PREFIX  
  
# install httpd runtime dependencies  
# see https://httpd.apache.org/docs/2.4/install.html#requirements  
RUN yum install \  
make \  
automake \  
gcc \  
autoconf \  
libtool \  
openssl-devel \  
pcre-devel \  
apr-devel \  
apr-util-devel \  
bzip2 \  
wget -y  
  
ENV HTTPD_VERSION 2.4.25  
ENV HTTPD_BZ2_URL
https://www.apache.org/dyn/closer.cgi?action=download&filename=httpd/httpd-$HTTPD_VERSION.tar.bz2  
  
RUN wget -O httpd.tar.bz2 "$HTTPD_BZ2_URL" \  
\  
&& mkdir -p src \  
&& tar -xf httpd.tar.bz2 -C src --strip-components=1 \  
&& rm httpd.tar.bz2 \  
&& cd src \  
\  
&& ./configure \  
\--prefix="$HTTPD_PREFIX" \  
\--enable-mods-shared=reallyall \  
&& make -j "$(nproc)" \  
&& make install \  
\  
&& cd .. \  
&& rm -r src man manual \  
\  
&& sed -ri \  
-e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \  
-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \  
"$HTTPD_PREFIX/conf/httpd.conf"  
  
# install ruby app environment ---------------------  
# install dependencies  
RUN yum install which \  
mysql \  
mysql-devel \  
lmygcc \  
nodejs \  
libcurl-devel -y  
  
# install rvm  
# see https://rvm.io/  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& curl -sSL https://get.rvm.io | bash -s stable  
  
# export rvm  
# ENV PATH /usr/local/rvm/bin:$PATH  
# install ruby  
RUN /bin/bash -l -c 'rvm install ruby-2.3.3'  
  
# export ruby  
RUN /bin/bash -l -c 'rvm use --default ruby-2.3.3'  
  
# install passenger  
RUN /bin/bash -l -c 'gem install passenger --version 5.1.1' \  
&& /bin/bash -l -c 'passenger-install-apache2-module --auto'  
  
# setup passenger config  
RUN echo -e 'LoadModule passenger_module
/usr/local/rvm/gems/ruby-2.3.3/gems/passenger-5.1.1/buildout/apache2/mod_passenger.so\n
\  
<IfModule mod_passenger.c>\n \  
PassengerRoot /usr/local/rvm/gems/ruby-2.3.3/gems/passenger-5.1.1\n \  
PassengerDefaultRuby /usr/local/rvm/gems/ruby-2.3.3/wrappers/ruby\n \  
</IfModule>' > /usr/local/apache2/conf/extra/passenger.conf \  
&& sed -i '$a Include conf/extra/passenger.conf'
/usr/local/apache2/conf/httpd.conf \  
&& mkdir /usr/local/apache2/conf/client \  
&& sed -i '$a Include conf/client/*.conf' /usr/local/apache2/conf/httpd.conf  
  
# install bundle  
RUN /bin/bash -l -c 'gem install bundle'  
  
COPY httpd-foreground /usr/local/bin/  
  
RUN chown httpd24:httpd24 /usr/local/bin/httpd-foreground \  
&& chmod 777 /usr/local/bin/httpd-foreground  
  
EXPOSE 80  
CMD ["/usr/local/bin/httpd-foreground"]  

