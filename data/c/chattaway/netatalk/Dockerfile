FROM chattaway/nslcd:latest  
  
ENV NETATALK_VERSION 3.1.11  
RUN yum install -y \  
cracklib-devel \  
gcc \  
krb5-devel \  
libacl-devel \  
libdb-devel \  
libevent-devel \  
libgcrypt-devel \  
libtdb-devel \  
make \  
openldap-devel \  
openssl-devel \  
pam-devel \  
quota-devel \  
tcp_wrappers-devel \  
&& yum clean all  
  
RUN curl -SL
http://downloads.sourceforge.net/project/netatalk/netatalk/$NETATALK_VERSION/netatalk-$NETATALK_VERSION.tar.gz
| tar -xz  
  
WORKDIR /netatalk-$NETATALK_VERSION  
RUN ./configure \  
\--without-libevent \  
\--without-tdb \  
\--with-cracklib \  
\--with-pam-confdir=/etc/pam.d \  
&& make install  
  
WORKDIR /  
RUN rm -fr /netatalk-$NETATALK_VERSION  
  
RUN mkdir --parents /run/lock  
  
COPY ./supervisord.conf /etc/supervisord.conf  
  
CMD ["supervisord", "--configuration", "/etc/supervisord.conf"]  
  
EXPOSE 548  
VOLUME ["/usr/local/etc"]  

