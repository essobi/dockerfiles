#  
# Dockerfile based on work of https://hub.docker.com/_/ubuntu-upstart/  
# and inspired by https://github.com/okvic77/docker-airtime  
#  
FROM ubuntu:14.04  
# ENV LANG en_US.UTF-8  
# ENV LANGUAGE en_US:en  
# ENV LC_ALL en_US.UTF-8  
ENV HOSTNAME localhost  
ENV DEBIAN_FRONTEND=noninteractive  
# let Upstart know it's in a container  
ENV container docker  
  
MAINTAINER Hans-Joachim  
  
#  
# Install some rudimental stuff  
RUN locale-gen --purge en_US.UTF-8 \  
&& update-locale LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8 \  
&& apt-get update && apt-get dist-upgrade -y \  
&& apt-get install -y python-psycopg2 nano \  
git rabbitmq-server apache2 curl postgresql postgresql-contrib  
#  
# Install libretime  
#  
COPY help/prep_os.sh /prep_os.sh  
RUN /prep_os.sh  
  
ADD init-fake.conf /etc/init/fake-container-events.conf  
  
# undo some leet hax of the base image  
RUN rm /usr/sbin/policy-rc.d; \  
rm /sbin/initctl; dpkg-divert --rename --remove /sbin/initctl  
  
# remove some pointless services  
RUN /usr/sbin/update-rc.d -f ondemand remove; \  
for f in \  
/etc/init/u*.conf \  
/etc/init/mounted-dev.conf \  
/etc/init/mounted-proc.conf \  
/etc/init/mounted-run.conf \  
/etc/init/mounted-tmp.conf \  
/etc/init/mounted-var.conf \  
/etc/init/hostname.conf \  
/etc/init/networking.conf \  
/etc/init/tty*.conf \  
/etc/init/plymouth*.conf \  
/etc/init/hwclock*.conf \  
/etc/init/module*.conf\  
; do \  
dpkg-divert --local \--rename --add "$f"; \  
done; \  
echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab  
  
#  
# copy the script for the 1st run  
#  
COPY 1st_start.conf /etc/init  
  
VOLUME ["/etc/airtime", "/var/lib/postgresql", "/srv/airtime/stor",
"/srv/airtime/watch"]  
  
EXPOSE 80 8000  
CMD ["/sbin/init"]  

