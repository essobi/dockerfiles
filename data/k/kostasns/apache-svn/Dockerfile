FROM debian:wheezy  
MAINTAINER Kostas <kostas@nuclearshoebox.com>  
  
ENV SVN_REPO_HOME /var/svn  
ENV SVN_AUTH_FILE ${SVN_REPO_HOME}/svn-auth  
  
ENV TINI_VERSION v0.10.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
  
COPY svn /tmp/svn  
COPY wandisco-debian.gpg /tmp/wandisco-debian.gpg  
  
#Add wandisco repo to install SVN 1.7 from  
RUN apt-key add /tmp/wandisco-debian.gpg \  
&& echo "deb http://opensource.wandisco.com/debian/ wheezy svn17" >
/etc/apt/sources.list.d/wandisco-subversion.list \  
  
#Install necessary software  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
subversion \  
libapache2-svn \  
  
#Clean cache  
&& apt-get clean && apt-get autoclean \  
  
#Apache and SVN configugration  
&& mkdir "${SVN_REPO_HOME}" && touch "${SVN_AUTH_FILE}" \  
&& chown -R www-data:www-data "${SVN_REPO_HOME}" \  
&& mv /tmp/svn /etc/apache2/sites-available/svn \  
&& a2enmod dav_svn && a2ensite svn && a2dissite 000-default \  
  
#Dirty way to change the values to ENV ones.  
#If anyone knows a better one, I'd appreciate the info.  
&& sed -i "s|SVN_REPO_HOME|${SVN_REPO_HOME}|g" /etc/apache2/sites-
available/svn \  
&& sed -i "s|SVN_AUTH_FILE|${SVN_AUTH_FILE}|g" /etc/apache2/sites-
available/svn \  
  
#Setting tini to be executable and final clean of the cache and temp folders  
&& chmod +x /bin/tini \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ${SVN_REPO_HOME}  
EXPOSE 80 443  
ENTRYPOINT ["/bin/tini", "--"]  
CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]  

