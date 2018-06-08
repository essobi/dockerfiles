FROM php:5.6-apache  
  
EXPOSE 80  
LABEL description="FirebirdWebAdmin 3.4.0 webbased interface to a firebird sql
server"  
LABEL maintainer="marian.aldenhoevel@marian-aldenhoevel.de"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
WORKDIR /app  
  
RUN \  
rm /etc/apache2/mods-available/php5.load \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends php5-interbase libapache2-mod-
php5 git-core firebird2.5-classic-common \  
&& php5enmod interbase \  
&& ln -s /usr/bin/isql-fb /usr/bin/isql \  
&& git clone git://github.com/mariuz/firebirdwebadmin.git . \  
&& ln -s /app /var/www/html/firebirdwebadmin \  
&& rm -rf .git \  
&& apt-get purge -y git git-core git-man libcurl3-gnutls liberror-perl \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Stuff we want for debugging  
#RUN \  
# apt-get update \  
# && apt-get install -y --no-install-recommends iputils-ping telnet nano file
net-tools curl procps  
ADD . ./  

