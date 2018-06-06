FROM centos:7  
RUN yum install -y epel-release \  
&& yum update -y \  
&& yum install -y \  
freetype freetype-devel gcc gd gd-devel giflib giflib-devel httpd libjpeg
libjpeg-devel libpng \  
libpng-devel make mod_perl perl perl-Cache-Cache perl-Cache-Memcached perl-CGI
perl-CPAN \  
perl-CPANPLUS perl-Digest-SHA1 perl-Error perl-GD perl-Image-Base perl-Image-
Info \  
perl-IO-Compress-Zlib perl-libwww-perl perl-local-lib perl-LWP-Protocol-https
perl-Test-NoWarnings \  
perl-Test-Simple perl-Test-Tester perl-YAML tar wget zlib zlib-devel \  
&& yum -y clean all  
  
RUN mkdir /tmp/amf && cd $_ \  
&& wget http://search.cpan.org/CPAN/authors/id/S/SH/SHERZODR/Image-
Resize-0.5.tar.gz \  
&& wget http://search.cpan.org/CPAN/authors/id/A/AG/AGRUNDMA/Image-
Scale-0.08.tar.gz \  
&& wget http://search.cpan.org/CPAN/authors/id/T/TO/TONYC/Imager-1.002.tar.gz
\  
&& wget --content-disposition
http://sourceforge.net/projects/mobilefilter/files/ApacheMobileFilter/4.03/Apache2-ApacheMobileFilter-4.03.tar.gz/download
\  
&& SORT_CREATED="--format=single-column --sort=time --time=ctime --reverse" \  
&& for file in `ls *gz $SORT_CREATED`; do tar -zxf $file; done \  
&& sed -i 's/png_memcpy/memcpy/g' Image-Scale-0.08/src/png.c \  
&& for dir in `ls -d */ $SORT_CREATED`; do cd $dir && perl Makefile.PL && make
&& make install && cd ..; done \  
&& rm -rf /tmp/amf  
  
RUN mkdir /tmp/wurfl && cd $_ \  
&& wget --content-disposition
http://sourceforge.net/projects/wurfl/files/WURFL/2.3.5/wurfl-2.3.5.xml.gz/download
\  
&& gzip -d wurfl-2.3.5.xml.gz \  
&& mkdir -p /data/amf \  
&& mv wurfl-2.3.5.xml /data/amf/wurfl.xml \  
&& rm -rf /tmp/wurfl  
  
RUN sed -ri 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g;
s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g;' /etc/httpd/conf/httpd.conf  
  
RUN echo 'OPTIONS="-D FOREGROUND" ' >> /etc/sysconfig/httpd  
  
ENV APACHE_RUN_USER root  
ENV APACHE_RUN_GROUP root  
ENV APACHE_LOG_DIR /etc/httpd/logs  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apachectl"]  

