# ---------------------------------------------------------------------------  
# See the NOTICE file distributed with this work for additional  
# information regarding copyright ownership.  
#  
# This is free software; you can redistribute it and/or modify it  
# under the terms of the GNU Lesser General Public License as  
# published by the Free Software Foundation; either version 2.1 of  
# the License, or (at your option) any later version.  
#  
# This software is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU  
# Lesser General Public License for more details.  
#  
# You should have received a copy of the GNU Lesser General Public  
# License along with this software; if not, write to the Free  
# Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  
# 02110-1301 USA, or see the FSF site: http://www.fsf.org.  
# ---------------------------------------------------------------------------  
FROM tomcat:8-jre8  
  
# ____ ____ ____ ____ _ __ _  
# |_ _||_ _||_ _| |_ _|(_) [ | _ (_)  
# \\\ \\\ / / \\\ \\\ /\\\ / / __ | | / ] __  
# > `' < \\\ \\\/ \\\/ / [ | | '' < [ |  
# _/ /'`\\\ \\\\_ \\\ /\\\ / | | | |`\\\ \\\ | |  
# |____||____| \\\/ \\\/ [___][__| \\\\_][___]  
MAINTAINER Vincent Massol <vincent@massol.net>  
  
# Note: when using docker-compose, the ENV values below are overridden from
the .env file.  
# Install LibreOffice + other tools  
RUN apt-get update  
RUN apt-get --no-install-recommends -y install curl libreoffice unzip
libmysql-java  
# Install XWiki as the ROOT webapp context in Tomcat  
# Create the Tomcat temporary directory  
# Configure the XWiki permanent directory  
ENV XWIKI_VERSION=$xwikiVersion  
ENV XWIKI_URL_PREFIX
"http://maven.xwiki.org/releases/org/xwiki/enterprise/xwiki-enterprise-
web/\${XWIKI_VERSION}"  
# Note: To compute the sha256, download the binary and issue:  
# - Unix: sha256sum <binary name>  
# - Mac: shasum --algorithm 256 <binary name>  
ENV XWIKI_DOWNLOAD_SHA256 $xwikiSha256  
RUN rm -rf /usr/local/tomcat/webapps/*  
RUN mkdir -p /usr/local/tomcat/temp  
RUN mkdir -p /usr/local/xwiki/data  
RUN wget http://download.forge.ow2.org/xwiki/xwiki-enterprise-web-9.2.war  
RUN mv xwiki-enterprise-web-9.2.war xwiki.war  
RUN unzip -d /usr/local/tomcat/webapps/ROOT xwiki.war  
RUN rm -f xwiki.war  
  
# Copy the JDBC driver in the XWiki webapp  
RUN cp /usr/share/java/mysql-connector-java-*.jar
/usr/local/tomcat/webapps/ROOT/WEB-INF/lib/  
# Configure Tomcat. For example set the memory for the Tomcat JVM since the
default value is too small for XWiki  
COPY tomcat/setenv.sh /usr/local/tomcat/bin/  
  
# Setup the XWiki Hibernate configuration  
COPY xwiki/hibernate.cfg.xml /usr/local/tomcat/webapps/ROOT/WEB-
INF/hibernate.cfg.xml  
  
# Set a specific distribution id in XWiki for this docker packaging.  
#RUN sed -i 's/<id>org.xwiki.enterprise:xwiki-enterprise-
web/<id>org.xwiki.enterprise:xwiki-enterprise-docker/' \\\  
# /usr/local/tomcat/webapps/ROOT/META-INF/extension.xed  
COPY xwiki/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
VOLUME /usr/local/xwiki  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["xwiki"]  

