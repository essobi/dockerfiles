# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER John <teraproc.john@gmail.com>  
  
# non-interactive mode  
ENV DEBIAN_FRONTEND noninteractive  
  
# install OpenMPI  
ADD openmpi-1.8.4.tgz /usr/local/  
#RUN tar -xzf /install/openmpi-1.8.4.tgz -C /usr/local/  
RUN ln -s /usr/local/openmpi-1.8.4 /usr/local/openmpi  
ADD openmpi.sh /etc/profile.d/openmpi.sh  
RUN /bin/cp -rf /usr/local/openmpi/lib/* /usr/lib/  
  
# install R  
#RUN sed -i '/deb-src http:\/\/us-east-1.ec2.archive.ubuntu.com\/ubuntu\/
trusty main/a deb http:\/\/cran.utstat.utoronto.ca\/bin\/linux\/ubuntu
trusty\/' /etc/apt/sources.list  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
ADD r-public-key.asc /tmp/  
RUN apt-key add /tmp/r-public-key.asc  
RUN apt-get update -y  
RUN apt-get install -y language-pack-en  
RUN update-locale LANG=en_US.UTF-8  
RUN apt-get install -y r-base r-base-dev r-recommended libxml2-dev
libcurl4-gnutls-dev  
ADD install-packages.R /tmp/  
RUN LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH Rscript
/tmp/install-packages.R  
  
RUN mv /usr/local/lib/R/site-library/BatchJobs /usr/local/lib/R/site-
library/BatchJobs.ori  
ADD BatchJobs_20150903.tar.gz /usr/local/lib/R/site-library/  
RUN chown -Rf root:root /usr/local/lib/R/site-library/BatchJobs  
ADD Rprofile.site /etc/R/  
  
# fix issue of adding new user. Refer to https://github.com/sequenceiq/docker-
pam/blob/master/ubuntu-14.04/Dockerfile  
RUN apt-get -y build-dep pam  
RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam
&& dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb
libpam0g*.deb  
  
# install OpenLava compute  
# required by openlava  
RUN apt-get install -y tcl psmisc  
ADD openlava-3.0-0.x86_64.deb /tmp/  
RUN dpkg -i /tmp/openlava-3.0-0.x86_64.deb  
RUN ln -s /opt/openlava-3.0 /opt/openlava  
RUN sed -i "s/--skip-alias //" /opt/openlava/bin/openmpi-mpirun  
ADD lsf.cluster.openlava /opt/openlava/etc/  
ADD lsb.params /opt/openlava/etc/  
ADD lsb.hosts /opt/openlava/etc/  
RUN echo "LIM_COMPUTE_ONLY=y" >> /opt/openlava/etc/lsf.conf  
RUN echo "LSF_ROOT_REX=y" >> /opt/openlava/etc/lsf.conf  
RUN echo "LSF_LIM_IGNORE_CHECKSUM=y" >> /opt/openlava/etc/lsf.conf  
RUN mkdir /home/openlava/  
RUN chown -R openlava:openlava /home/openlava/  
RUN echo "openlava:openlava" | chpasswd  
ADD openlava /etc/init.d/  
RUN chmod +x /etc/init.d/openlava  
  
ADD userconf.sh /usr/bin/userconf.sh  
ADD add-students /usr/local/bin/add-students  
RUN chmod +x /usr/bin/userconf.sh /usr/local/bin/add-students  
  
# clean up installation file  
RUN rm -rf /tmp/*  
  
# Add R examples  
ADD *.csv /home/  
  
# open port number of LIM, SBATCHD, MBATCHD and RStudio  
EXPOSE 6879 6881 6882  
# To workaround some extremely strange tail -f behavior (which says "has been
replaced with a remote file. giving up on this name"), create and truncate log
file on start up  
# upstart in docker container doesn't work:
https://github.com/saltstack/salt/issues/11118  
CMD ["/bin/sh", "-c", "chmod 0777 /share/; /usr/bin/userconf.sh; echo
\"LSF_SERVER_HOSTS=`echo $MASTER`\" >> /opt/openlava/etc/lsf.conf; sed -i
\"s/MASTER_HOSTNAME/`echo $MASTER`/\" /opt/openlava/etc/lsf.cluster.openlava;
sed -i \"/`echo $MASTER`/a `hostname` ! ! 1 - -\"
/opt/openlava/etc/lsf.cluster.openlava; service openlava restart; .
/opt/openlava/etc/openlava.sh; /opt/openlava/bin/lsaddhost `hostname`; umask 0
&& truncate -s0 /opt/openlava/log/lim.log.`hostname`; tail -n0 -F
/opt/openlava/log/lim.log.`hostname`"]  
# build docker image and run docker container by  
# docker build -t olcompute .  
# run openlava compute  
# docker run -p 6879:6879 -p 6881:6881 -p 6882:6882 --uts="host" -v
/vagrant/share:/share --net=host -e "MASTER=$MASTERHOSTNAME" olcompute  
# test openlava by run docker exec -it $containerid /bin/bash  

