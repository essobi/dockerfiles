FROM amazonlinux:latest AS build  
MAINTAINER celeron1ghz <celeron1ghz@gmail.com>  
  
RUN yum -y groupinstall "Development Tools" \  
&& curl -sL https://raw.githubusercontent.com/tokuhirom/Perl-
Build/master/perl-build | perl - 5.26.1 /opt/perl-5.26/ \  
&& curl -sL https://cpanmin.us/ | /opt/perl-5.26/bin/perl - App::cpanminus
Carton  
  
  
FROM amazonlinux:latest  
COPY --from=build /opt/perl-5.26 /opt/perl-5.26  
  
RUN yum -y install curl python python-pip git zip memcached \  
&& curl -sL https://rpm.nodesource.com/setup_9.x | bash - \  
&& yum install -y nodejs gcc make \  
&& yum install -y openssl-devel expat-devel libxml2-devel mysql-devel \  
&& yum install -y libtiff-devel giflib-devel libpng-devel libjpeg-turbo-devel
freetype-devel \  
&& pip-python install awscli \  
&& yum clean all \  
&& rm -Rf /tmp/* \  
&& rm -Rf /var/cache/yum \  
&& rm -Rf /usr/share/man \  
&& rm -Rf /usr/share/doc \  
&& rm -Rf /usr/share/perl5/pod \  
&& rm -Rf /usr/lib/node_modules/npm/man \  
&& rm -Rf /usr/lib/node_modules/npm/doc \  
&& rm -Rf /usr/lib/node_modules/npm/html \  
&& rm -Rf /usr/lib/node_modules/npm/scripts \  
&& rm -Rf /opt/perl-5.26/man/ \  
&& rm -Rf /opt/perl-5.26/lib/5.26.1/pod \  
&& find / | grep '.pod$' | xargs rm \  
&& find / | grep -i 'README' | xargs rm  

