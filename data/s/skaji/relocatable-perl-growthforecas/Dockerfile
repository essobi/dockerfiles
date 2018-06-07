FROM skaji/relocatable-perl  
MAINTAINER Shoichi Kaji <skaji@cpan.org>  
  
RUN yum install -y xz gcc-c++ chrpath bzip2 patch  
  
RUN mkdir /tmp/build  
WORKDIR /tmp/build  
  
ADD misc/rrdtool-deps-install.pl /tmp/build/rrdtool-deps-install.pl  
RUN PREFIX=/opt/perl/local /usr/bin/perl rrdtool-deps-install.pl  
ADD misc/pango.modules /opt/perl/local/etc/pango/pango.modules  
  
RUN rm -rf /opt/perl/local/etc/fonts  
RUN mkdir -p /opt/perl/local/etc/fontconfig/conf.d
/opt/perl/local/share/fonts/truetype/dejavu /opt/perl/local/var/fontconfig  
RUN wget -q http://sourceforge.net/projects/dejavu/files/dejavu/2.34/dejavu-
fonts-ttf-2.34.tar.bz2  
RUN tar xjf dejavu-fonts-ttf-2.34.tar.bz2  
RUN cp dejavu-fonts-ttf-2.34/ttf/* /opt/perl/local/share/fonts/truetype/dejavu  
RUN cp dejavu-fonts-ttf-2.34/fontconfig/*
/opt/perl/local/share/fontconfig/conf.avail  
ADD misc/fonts.conf /opt/perl/local/etc/fontconfig/fonts.conf  
RUN cd /opt/perl/local/etc/fontconfig/conf.d && ln -s
../../../share/fontconfig/conf.avail/*.conf .  
  
RUN /opt/perl/bin/cpanm --installdeps -nq Alien::RRDtool@0.06  
  
ADD misc/Alien-RRDtool-0.06-patch /tmp/build/Alien-RRDtool-0.06-patch  
RUN wget -q http://www.cpan.org/authors/id/K/KA/KAZEBURO/Alien-
RRDtool-0.06.tar.gz  
RUN tar xzf Alien-RRDtool-0.06.tar.gz && \  
cd Alien-RRDtool-0.06 && \  
patch -p0 < /tmp/build/Alien-RRDtool-0.06-patch && \  
PKGCONFIG=/opt/perl/local/bin/pkg-config \  
PKG_CONFIG_PATH=/opt/perl/local/lib/pkgconfig \  
/opt/perl/bin/cpanm -nq .  
  
RUN chrpath -r \$ORIGIN/../../../../../../local/lib
/opt/perl/lib/site_perl/5.*/x86_64-linux/auto/RRDs/RRDs.so  
RUN /opt/perl/bin/perl -MRRDs -e0  
  
RUN /opt/perl/bin/cpanm -nq --installdeps GrowthForecast  
RUN /opt/perl/bin/cpanm -nq GrowthForecast  
  
# I don't know why: sometimes missing dist share files  
RUN if [ `find /opt/perl/lib/site_perl/5.*/auto/share/dist/GrowthForecast
-type f | wc -l` -eq 20 ]; then \  
echo GrowthForecast share files exist; \  
else \  
find /opt/perl/lib/site_perl/5.*/auto/share/dist/GrowthForecast -type f >&2;
perl -e 'die "some GrowthForecast files missing!\n"'; \  
fi  
  
ADD misc/header-growthforecast.pl /tmp/build/header-growthforecast.pl  
RUN /opt/perl/bin/perl /tmp/build/header-growthforecast.pl
/opt/perl/bin/growthforecast.pl  
  
RUN /opt/perl/bin/change-shebang -f /opt/perl/bin/*  
  
RUN cp -r /opt/perl /tmp/growthforecast-`/opt/perl/bin/perl -MConfig -e 'print
$Config{archname}'`  
RUN cd /tmp && tar czf /artifact/growthforecast-`/opt/perl/bin/perl -MConfig
-e 'print $Config{archname}'`.tar.gz \  
growthforecast-`/opt/perl/bin/perl -MConfig -e 'print $Config{archname}'`  
  
RUN rm -rf /tmp/growthforecast-`/opt/perl/bin/perl -MConfig -e 'print
$Config{archname}'`  
RUN rm -rf /tmp/build  
  
CMD ["sleep", "infinity"]  

