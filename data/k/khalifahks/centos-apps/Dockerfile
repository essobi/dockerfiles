FROM khalifahks/centos-php  
  
# Install yarn RPMs and GPG keys  
RUN curl -sS https://dl.yarnpkg.com/rpm/yarn.repo >>
/etc/yum.repos.d/yarn.repo \  
&& curl -sS https://dl.yarnpkg.com/rpm/pubkey.gpg >> /etc/pki/rpm-gpg/RPM-GPG-
KEY-yarn \  
&& rpm --import etc/pki/rpm-gpg/RPM-GPG-KEY-yarn \  
&& echo "sslverify=false" >> /etc/yum.conf \  
&& curl -sSk https://rpm.nodesource.com/pub_9.x/el/7/x86_64/nodesource-
release-el7-1.noarch.rpm >> ./nodesource-release-el7-1.noarch.rpm \  
&& yum -y install --nogpgcheck ./nodesource-release-el7-1.noarch.rpm  
  
RUN yum -y update \  
&& yum -y install git \  
php-pecl-xdebug \  
nodejs \  
yarn \  
firefox \  
java-1.8.0-openjdk \  
make \  
gcc-c++ \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& mkdir -p code  
  
ADD ./rebased-check.sh /bin/rebased-check.sh  
  
RUN echo "export CLICOLOR=1" >> /root/.bashrc \  
&& echo 'export GREP_OPTIONS="--color=auto --exclude-dir=.git --exclude-
dir=.idea"' >> /root/.bashrc \  
&& chmod a+x /bin/rebased-check.sh  
  
WORKDIR code  
  
# docker build --rm -t khalifahks/centos-apps ./apps  
# docker run -d --rm --name centos-apps khalifahks/centos-apps  
# docker run -it --rm --name centos-apps khalifahks/centos-apps  
# docker run --rm --name centos-apps khalifahks/centos-apps  
# docker exec -it centos-apps bash  
# Start PHP-FPM server and tail the logs.  
ENTRYPOINT ["start-php-fpm.sh"]

