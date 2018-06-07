#
=============================================================================  
# mykro/java8-jre - A build on top of Debian 8 (Jessie)  
#
-----------------------------------------------------------------------------  
# Copyright (C) 2015 Matt Hartstonge  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
# Java is provided by Oracle and as such, by using of this container, you  
# agree to Oracle's JRE License as well.  
#
=============================================================================  
FROM debian:jessie  
MAINTAINER Matt Hartstonge <matt@mykro.co.nz>  
  
ENV JAVA_VERSION "8u72"  
ENV BUILD_VERSION "b15"  
ENV JDK_VERSION "1.8.0_72"  
  
RUN apt-get update && apt-get install -y \  
wget \  
curl \  
&& mkdir -p /usr/lib/jvm \  
&& cd /usr/lib/jvm \  
&& wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-${BUILD_VERSION}/server-
jre-${JAVA_VERSION}-linux-x64.tar.gz" \  
&& tar -zxvf server-jre-${JAVA_VERSION}-linux-x64.tar.gz \  
&& rm /usr/lib/jvm/server-jre-${JAVA_VERSION}-linux-x64.tar.gz \  
&& ln -s /usr/lib/jvm/jdk${JDK_VERSION}/bin/java /bin/ \  
&& cd /usr/lib/jvm/jdk${JDK_VERSION} \  
&& find . -type f -name '*.html' -delete \  
&& find . -type f -name '*.bat' -delete \  
&& find . -type f -name 'COPYRIGHT' -delete \  
&& find . -type f -name 'LICENSE' -delete \  
&& find . -type f -name 'NOTICE' -delete \  
&& find . -type f -name '3RDPARTY' -delete \  
&& find . -type f -name 'THIRDPARTYLICENSE.txt' -delete \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

