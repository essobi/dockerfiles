FROM halplatform/hal-build-environments:php7.0-centos7  
### docker build -t lci ./.circleci  
### Install git-core if running locally  
  
#TODO do i need this?  
#RUN curl -sLk https://git/pages/circleci/prepare-environment/prepare.sh |
bash -  
  
# Install yarn RPMs and GPG keys  
RUN curl -sS https://dl.yarnpkg.com/rpm/yarn.repo >>
/etc/yum.repos.d/yarn.repo \  
&& curl -sS https://dl.yarnpkg.com/rpm/pubkey.gpg >> /etc/pki/rpm-gpg/RPM-GPG-
KEY-yarn \  
&& rpm --import etc/pki/rpm-gpg/RPM-GPG-KEY-yarn \  
&& wget --no-check-certificate https://dl.google.com/linux/direct/google-
chrome-stable_current_x86_64.rpm \  
&& yum -y install nodejs \  
firefox \  
java-1.8.0-openjdk \  
nginx \  
php-mcrypt \  
google-chrome-stable_current_x86_64.rpm \  
yarn \  
make \  
libsass \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin  
  
# docker build --rm --no-cache -t khalifahks/wci ./wci  
# docker build --rm -t khalifahks/wci ./wci  
# docker run -d --rm -p 9000:9000 --name wci -h centos_php khalifahks/wci  
# docker run -it --rm -p 9000:9000 --name wci -h centos_php khalifahks/wci  
# docker exec -it wci bash  
# cp from docker  
# docker cp centos-apps:/etc/php.d/15-xdebug.ini ./wci/

