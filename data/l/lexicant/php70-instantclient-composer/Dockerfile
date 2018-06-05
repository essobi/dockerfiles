# Can't use alpine here without a lot of work. Seems like there are work
arounds but in short there are several  
# issues in various projects that boil down to alpine using musl and not
compileing correctly.  
# https://github.com/kubo/ruby-oci8/issues/129  
FROM php:7.1-cli-jessie  
  
ENV ORACLE_HOME="/usr/lib/oracle/12.2/client64/lib"  
# Oracle makes these a pain in the ass and has http auth for the files. Just
package them locally  
# until we can switch this to curl/wget and put in package name variables.  
COPY oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm /app/  
COPY oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm /app/  
COPY oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm /app/  
  
WORKDIR /app  
  
# alien and systemtap-sdt-dev are for building instantclient.  
# libio1 is for php and dynamic libraries.  
# zip, unzip, and git are for composer. These (noted later) should probably go
in their own layer.  
RUN apt-get update \  
&& apt-get install -y alien systemtap-sdt-dev libaio1 zip unzip git  
  
RUN alien -i oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm  
RUN alien -i oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm  
RUN alien -i oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm  
  
RUN echo "$ORACLE_HOME" | tee /etc/ld.so.conf.d/oracle.conf ldconfig  
  
# Directory isn't created from the rpm installs, probalby since the package is
for rhel/centos.  
# We could fix this by using the zip file. Alien is a bit slow as well so it
might make sense to refactor this  
# and use the zip file instead.  
RUN mkdir -p $ORACLE_HOME  
  
# Setting environment variables it was difficult to get pecl to install as
many of the stackover flow results  
# indicated. I choose to pipe the pecl input here. The following is a list of
various env variable fixes that  
# were listed on various stackoverflow questions. None of these worked in my
case however they may be a better  
# solution to running the pecl install. I don't have enough domain knowladge
over instantclient to know what  
# the best soution going forward might be.  
# ENV FORCE_RPATH=1  
# ENV ORACLE_HOME="/usr/lib/oracle/12.2/client64/lib"  
# ENV LD_LIBRARY_PATH="/usr/lib/oracle/12.2/client64"  
# ENV OCI_LIB="/usr/lib/oracle/12.2/client64/lib"  
# ENV TNS_ADMIN="/usr/lib/oracle/12.2/client64/network/admin"  
# ENV C_INCLUDE_PATH="/usr/lib/oracle/12.2/client64"  
# ENV PHP_DTRACE=yes  
# Also if we're thinking about long term maintainibility and not simplicty the
next part of this file should probably  
# be it's own container, built FROM my-image-registry:php70-oci8. For now
though it doesn't hurt  
# to have them combined.  
RUN echo "instantclient,$ORACLE_HOME" | pecl install oci8  
  
# Add our extention to conf.d so php is aware of it.  
RUN echo "extension = oci8.so" >> /usr/local/etc/php/conf.d/oci8.ini  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/bin/ --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
ENTRYPOINT ["/bin/composer"]  
  
# Usage:  
# docker build -t project-name-composer ./docker/phpcli/  
# docker run -v $(pwd):/app -ti --rm project-name-composer install  
# Note: project-name is arbitrary however with this naming I think it will be
more natural to remember the container  
# name.  

