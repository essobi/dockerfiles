FROM balasys/zorpgpl  
  
MAINTAINER Szilárd Pfeiffer "coroner@pfeifferszilard.hu"  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
devscripts \  
equivs \  
git-core  
RUN git clone -b 6.0.11.0 https://github.com/Balasys/libzorpll.git
/usr/src/libzorpll \  
&& git clone -b 6.0.11 https://github.com/Balasys/zorp.git /usr/src/zorp \  
&& mk-build-deps -i -t "apt-get -o Debug::pkgProblemResolver=yes --yes --no-
install-recommends" /usr/src/libzorpll/debian/control \  
&& mk-build-deps -i -t "apt-get -o Debug::pkgProblemResolver=yes --yes --no-
install-recommends" /usr/src/zorp/debian/control  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/tmp/* \  
&& rm -rf /tmp/*  
  
RUN cd /usr/src/libzorpll \  
&& ./autogen.sh \  
&& ./configure --enable-debug \  
\--prefix=/usr \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--sysconfdir=/etc \  
\--libexecdir=/usr/libzorpll \  
&& make \  
&& make check \  
&& make install  
  
RUN cd /usr/src/zorp \  
&& ./autogen.sh \  
&& ./configure --enable-debug \  
\--prefix=/usr \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--localstatedir=/var/lib/zorp \  
\--sysconfdir=/etc \  
\--with-pidfiledir=/var/run/zorp/ \  
&& make \  
&& make check \  
&& make install  

