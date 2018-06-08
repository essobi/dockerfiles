FROM petervanderdoes/buildenv:trusty  
  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
# Upstart and DBus have issues inside docker. Work around it  
#RUN dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
  
RUN apt-get update  
  
# Installing the build environment  
RUN apt-get install -y libz-dev libpcre3-dev gettext \  
libcurl4-gnutls-dev libexpat1-dev \  
subversion libsvn-perl libyaml-perl \  
tcl \  
libhttp-date-perl \  
python \  
cvs cvsps libdbd-sqlite3-perl \  
unzip libio-pty-perl \  
dh-exec apache2-dev \  
dpkg-dev  

