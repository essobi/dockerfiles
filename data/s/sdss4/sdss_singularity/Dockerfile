# sdss/sdss_singularity  
FROM ubuntu:16.04  
MAINTAINER Joel Brownstein <joelbrownstein@astro.utah.edu>  
LABEL build="Ubuntu 16.04 with nginx-extras (Aug 13, 2017 12:36MDT)"  
  
# ========================================================  
# WEBSERVER> nginx-extras  
# ========================================================  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu wily main universe" >
/etc/apt/sources.list.d/nginx-stable.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C \  
&& apt-get update \  
&& apt-get install -y nginx-extras  
  
# ========================================================  
# USERS > admin  
# ========================================================  
RUN apt-get update \  
&& apt-get install -y sudo vim nano rsyslog subversion lmod tclsh build-
essential openssh-server bzip2 git postgresql-client uwsgi \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /uufs  
RUN mkdir -p /tmp/bin  
ADD users/admin/tmp/bin /tmp/bin/  
RUN chmod +x /tmp/bin/*  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
\  
&& sed -i 's/Port 22/Port 50022/' /etc/ssh/sshd_config \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin no/'
/etc/ssh/sshd_config \  
&& sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/cron \  
&& sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/sshd \  
&& ln -s /usr/share/lmod/lmod/init/env_modules_python.py
/usr/share/lmod/lmod/init/python \  
&& touch /root/.Xauthority \  
&& true  
  
# Add Users and Groups  
RUN groupadd sdss \  
&& chmod -x /etc/update-motd.d/*  
ADD users/admin/etc/motd /etc/motd  
  
RUN useradd -g sdss sdssadmin \  
&& chsh -s /bin/bash sdssadmin \  
&& passwd -d sdssadmin \  
&& mkdir /home/sdssadmin \  
&& addgroup sdssadmin sdss \  
&& addgroup sdssadmin staff \  
&& true  
ADD users/admin/home/sdssadmin /home/sdssadmin/  
#RUN chown -R sdssadmin:sdss /home/sdssadmin \  
RUN echo "sdssadmin ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& echo "sdssadmin ALL=(ALL) NOPASSWD: /usr/bin/rsync --daemon" >>
/etc/sudoers \  
&& echo "sdssadmin ALL=(ALL) NOPASSWD: /etc/init.d/xinetd *" >> /etc/sudoers \  
&& echo "sdssadmin ALL=(ALL) NOPASSWD: /usr/sbin/service nginx *" >>
/etc/sudoers \  
&& echo "sdssadmin ALL=(ALL) NOPASSWD: /usr/sbin/service cron *" >>
/etc/sudoers \  
&& echo "sdssadmin ALL=(ALL) NOPASSWD: /usr/sbin/service rsyslog *" >>
/etc/sudoers  
  
ENV SSH_KEY ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDHQ/qcYdnnlKUy295NZQBrq3kiv4u34W+8AEPRe35/RppAy/wYmaTMK0oE7NXFnatxA+7sFz8BOfHI4si5MHt/wn8tgB8XteSMmYFgLi9BExMlx+7q9jt6tMzUy7gYdx6sh9KCS5hoH8HSt2E5MoZK57UqUMMMaBfcWvBYyt0y+WXujTN1AliAgnI3VdywZP8/k4UQ4K+FwTYSOt3bSzmtD/YdD8ngk+2DSpjASl/1Z16ESz6jYJxqvBhdgT81Q6+Bp8/K8NQrXfKJHNWW1P3yTe5m+DI7LvDu8Bae3fSMvuq4/Vce0Et1HTEvVebCinPO0xmrg3j9LvFtqvVjZjvl
joel@dhn  
  
# ========================================================  
# HOST > data  
# ========================================================  
RUN apt-get update \  
&& apt-get install -y xinetd rsync \  
&& apt-get install -y python-software-properties \  
&& apt-get install -y python2.7 \  
&& apt-get install -y locales \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD host/data/etc/rsyncd.conf /etc/rsyncd.conf  
ADD host/data/etc/timezone /etc/timezone  
ADD host/data/etc/xinet.d/rsync /etc/xinet.d/rsyncd.conf  
ADD host/data/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD host/data/etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf  
ADD host/data/software /software  
  
RUN chmod g+w,o+rw /etc/rsyncd.conf \  
&& chmod g+w,o+rw /etc/xinet.d/rsyncd.conf \  
&& chmod -R g+w,o+rw /etc/nginx/nginx.conf \  
&& chmod -R g+w,o+rw /etc/nginx/conf.d \  
&& ln -fs /usr/share/zoneinfo/US/Mountain /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& locale-gen en_US.UTF-8  
  
# ========================================================  
# PYTHON> miniconda  
# ========================================================  
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
# wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-4.3.11-Linux-x86_64.sh -O
/tmp/miniconda.sh && \  
# /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \  
# rm /tmp/miniconda.sh  
#RUN /opt/conda/bin/conda update conda && \  
# /opt/conda/bin/conda install ipython  
EXPOSE 22 80 443 873  
CMD ["/tmp/bin/start_services"]  
  

