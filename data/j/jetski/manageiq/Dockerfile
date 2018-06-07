FROM centos:7  
ENV container docker  
  
# Set locale manually on build (docker defaults to POSIX which causes initdb
to set the wrong db encoding, MIQ must have UTF8)  
# Once systemd is online, it will set locale based /etc/locale.conf  
# Only needed if building with docker-1.8  
ENV LANG en_US.UTF-8  
# Install EPEL repo, yum necessary packages for the build without docs, clean
all caches (no DNF)  
RUN yum install -y epel-release && rpm -ivh
http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-1.noarch.rpm \  
&& yum -y install --setopt=tsflags=nodocs nodejs tar sudo git memcached
postgresql94-devel postgresql94-server \  
libxml2-devel libxslt-devel patch gcc-c++ openssl-devel gnupg curl which net-
tools libyaml-devel \  
autoconf readline-devel libffi-devel bzip2 automake libtool bison sqlite-devel
cmake; yum clean all  
  
ENV PATH
$PATH:/usr/pgsql-9.4/bin/:/usr/local/rvm/gems/ruby-2.2.3/bin/:/usr/local/rvm/bin  
  
# Systemd cleanups, setup volumes  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# Required to allow systemd to run in non-privileged container. It is required
to mount it as a volume  
# docker run -d -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 3000:3000
<image_name>  
VOLUME [ "/sys/fs/cgroup" ]  
  
# POSTGRESQL INIT  
# Do not call a login "-" su, resets the ENV  
RUN su postgres -c 'initdb -D /var/lib/pgsql/data'  
## 2. RVM  
# Download and install RVM, setup environment, install ruby/gems, clean all  
# Note: RVM uses yum to bring missing pre-reqs  
  
RUN /usr/bin/curl -sSL https://rvm.io/mpapis.asc | gpg2 --import - &&
/usr/bin/curl -sSL https://get.rvm.io \  
| rvm_tar_command=tar bash -s stable && source /etc/profile.d/rvm.sh \  
&& echo "gem: --no-ri --no-rdoc --no-document" > ~/.gemrc \  
&& /bin/bash -l -c "rvm requirements ; rvm install ruby 2.2.3 ; rvm use 2.2.3
--default ; \  
gem install bundler rake ; gem install nokogiri -- --use-system-libraries ; \  
rvm cleanup all ; yum clean all ; rvm disk-usage all"  
  
# GIT clone and prepare services (shallow clone)  
RUN mkdir /manageiq && git clone --depth 1
https://github.com/ManageIQ/manageiq /manageiq  
  
# Change workdir to clone, prepare database, start it, run setup, shutdown and
cleanup all  
WORKDIR /manageiq  
#COPY docker-assets/docker_setup bin/docker_setup  
RUN su postgres -c "pg_ctl -D /var/lib/pgsql/data start" && sleep 5 \  
&& su postgres -c "psql -c \"CREATE ROLE root SUPERUSER LOGIN PASSWORD
'smartvm'\"" \  
&& su postgres -c "pg_ctl -D /var/lib/pgsql/data stop"  
  
RUN su postgres -c "pg_ctl -D /var/lib/pgsql/data start" \  
&& /bin/bash -l -c "/usr/bin/memcached -u memcached -p 11211 -m 64 -c 1024 -l
127.0.0.1 &" \  
&& /bin/bash -l -c "bin/setup" && su postgres -c "pg_ctl -D
/var/lib/pgsql/data stop" \  
&& pkill memcached && /bin/bash -l -c "rvm cleanup all ; rm -vf
$(/usr/local/rvm/bin/rvm gemdir)/cache/* ; rvm disk-usage all"  
# Copy evmserver startup script and systemd evmserverd unit file  
COPY docker-assets/evmserver.sh bin/evmserver.sh  
COPY docker-assets/evmserverd.service
/usr/lib/systemd/system/evmserverd.service  
RUN sed -i s#PGDATA=/var/lib/pgsql/9.4/data/#PGDATA=/var/lib/pgsql/data/#g
/usr/lib/systemd/system/postgresql-9.4.service  
RUN chmod +x bin/evmserver.sh  
  
# Enable services on systemd  
RUN systemctl enable evmserverd memcached postgresql-9.4  
RUN source /etc/profile.d/rvm.sh  
  
# Expose required container ports  
EXPOSE 3000 4000  
# Call systemd to bring up system  
CMD [ "/usr/sbin/init" ]  

