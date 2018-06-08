FROM ubuntu:14.04  
MAINTAINER Ascensio System SIA <support@onlyoffice.com>  
  
ARG RELEASE_DATE="2016-06-21"  
ARG RELEASE_DATE_SIGN=""  
ARG VERSION="8.9.0.190"  
ARG SOURCE_REPO_URL="deb
http://static.teamlab.com.s3.amazonaws.com/repo/debian squeeze main"  
LABEL onlyoffice.community.release-date="${RELEASE_DATE}" \  
onlyoffice.community.version="${VERSION}" \  
onlyoffice.community.release-date.sign="${RELEASE_DATE_SIGN}"  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN echo "${SOURCE_REPO_URL}" >> /etc/apt/sources.list && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys CB2DE8E5 &&
\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
DEBIAN_FRONTEND=noninteractive && \  
locale-gen en_US.UTF-8 && \  
apt-get -y update && \  
apt-get install --force-yes -yq software-properties-common wget cron rsyslog
&& \  
wget http://nginx.org/keys/nginx_signing.key && \  
apt-key add nginx_signing.key && \  
echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>
/etc/apt/sources.list.d/nginx.list && \  
echo "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>
/etc/apt/sources.list.d/nginx.list && \  
add-apt-repository -y ppa:builds/sphinxsearch-rel22 && \  
echo "Start=No" >> /etc/init.d/sphinxsearch && \  
apt-get -y update && \  
apt-get install --force-yes -yq mono-complete ca-certificates-mono
apache2-utils realpath rsync openssh-server && \  
echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && \  
apt-get install --force-yes -yq dumb-init sphinxsearch onlyoffice-
communityserver htop nano dnsutils && \  
rm -rf /var/lib/apt/lists/*  
  
ADD config /app/onlyoffice/setup/config/  
ADD assets /app/onlyoffice/setup/assets/  
ADD run-community-server.sh /app/onlyoffice/run-community-server.sh  
RUN chmod -R 755 /app/onlyoffice/*.sh  
RUN bash -c "source /app/onlyoffice/setup/config/build.sh;\  
perm_change_ugid onlyoffice 1500; \  
perm_change_ugid mysql 1501;"  
RUN chown onlyoffice:onlyoffice /app/onlyoffice/setup/config/icon/*;\  
cp /app/onlyoffice/setup/config/googleeac863c2413debac.html
/var/www/onlyoffice/WebStudio; \  
rm /var/www/onlyoffice/WebStudio/googleb46d076df2fc5934.html; \  
chmod 444 /app/onlyoffice/setup/config/icon/*; \  
cp -af /app/onlyoffice/setup/config/icon/*
/var/www/onlyoffice/WebStudio2/skins/default/Images/onlyoffice_logo;\  
cp -af /app/onlyoffice/setup/config/icon/*
/var/www/onlyoffice/WebStudio/skins/default/Images/onlyoffice_logo;  
VOLUME ["/var/log/onlyoffice"]  
VOLUME ["/var/www/onlyoffice/Data"]  
VOLUME ["/var/lib/mysql"]  
VOLUME ["/media/davsonnt"]  
  
EXPOSE 80 443 5222 3306 9865 9888 9866 9871 9882 5280  
CMD exec dumb-init bash --rcfile /app/onlyoffice/run-community-server.sh -i;  

