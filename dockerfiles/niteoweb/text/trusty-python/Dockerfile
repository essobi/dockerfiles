from   ubuntu:trusty
env    DEBIAN_FRONTEND noninteractive

run apt-get -y --force-yes update
run apt-get -y --force-yes upgrade
run apt-get -y --force-yes install software-properties-common curl git wget unzip nano build-essential autoconf libxml2-dev libssl-dev libbz2-dev libcurl3-dev libdb5.1-dev libjpeg-dev libpng-dev libXpm-dev libfreetype6-dev libt1-dev libgmp3-dev libc-client-dev libldap2-dev libmcrypt-dev libmhash-dev freetds-dev libz-dev libmysqlclient15-dev ncurses-dev libpcre3-dev libsqlite-dev libaspell-dev libreadline6-dev librecode-dev libsnmp-dev libtidy-dev libxslt-dev libt1-dev 
run apt-get -y --force-yes install ruby-dev debhelper python3-dev python3-setuptools devscripts libxml2-dev
run apt-get autoclean
run apt-get -y --force-yes install python-pip python-setuptools libpython-dev
run locale-gen en_US.UTF-8
run add-apt-repository "deb http://repo.aptly.info/ squeeze main" -y
run apt-key adv --keyserver keys.gnupg.net --recv-keys E083A3782A194991
run apt-get update
run apt-get -yq --force-yes install dh-virtualenv goaccess aptly
