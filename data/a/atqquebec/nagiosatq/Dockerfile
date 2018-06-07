FROM centos:centos7  
MAINTAINER gardar@ok.is  
  
# - Install basic packages (e.g. python-setuptools is required to have
python's easy_install)  
# - Install yum-utils so we have yum-config-manager tool available  
# - Install inotify, needed to automate daemon restarts after config file
changes  
# - Install jq, small library for handling JSON files/api from CLI  
# - Install supervisord (via python's easy_install - as it has the newest 3.x
version)  
run yum update -y  
run yum install -y epel-release  
run yum install -y iproute python-setuptools hostname inotify-tools yum-utils
which jq mod_ssl openssl  
run yum clean all  
run easy_install supervisor  
  
ENV ADAGIOS_HOST nagiosatq.local  
ENV ADAGIOS_USER nagiosadmin  
ENV ADAGIOS_PASS nagiosadmin  
  
# First install the opensource.is and consol labs repositories  
RUN rpm -ihv http://opensource.is/repo/ok-release.rpm  
RUN rpm -Uvh https://labs.consol.de/repo/stable/rhel7/x86_64/labs-consol-
stable.rhel7.noarch.rpm  
RUN yum install -y epel-release  
RUN yum update -y ok-release  
RUN yum clean all && yum -y update  
  
#  
# Install Deps  
#  
RUN yum install -y git acl libstdc++-static python-setuptools facter mod_wsgi
postfix python-pip sudo  
RUN pip install --upgrade pip  
  
# Install Nagios 4  
#  
RUN yum install -y nagios nagios-plugins-all pnp4nagios  
  
#  
# Enable and start services  
#  
RUN systemctl enable nagios  
RUN chkconfig npcd on  
RUN systemctl enable httpd  
  
#  
# Install Livestatus  
#  
RUN yum install -y check-mk-livestatus  
# Add check_mk livestatus broker module to nagios config  
RUN echo "broker_module=/usr/lib64/check_mk/livestatus.o
/var/spool/nagios/cmd/livestatus debug=1" >> /etc/nagios/nagios.cfg  
  
#  
# Install Remote Livestatus service  
# Needs livestatus xinetd config below  
#  
RUN yum install -y xinetd  
ADD container-files/etc/xinetd.d/livestatus /etc/xinetd.d/livestatus  
  
# Lets make sure adagios can write to nagios configuration files, and that  
# it is a valid git repo so we have audit trail  
WORKDIR /etc/nagios  
RUN git init /etc/nagios/  
RUN git config user.name "User"  
RUN git config user.email "email@mail.com"  
RUN git add *  
RUN git commit -m "Initial commit"  
  
# Make sure nagios group will always have write access to the configuration
files:  
RUN chown -R nagios:nagios /etc/nagios/* /etc/nagios/.git  
  
# Install Pynag from Git  
RUN mkdir -p /opt/pynag  
WORKDIR /opt/  
RUN pip install django==1.6  
RUN pip install simplejson  
RUN git clone git://github.com/pynag/pynag.git  
  
# Install Adagios from Git  
RUN mkdir -p /opt/adagios  
WORKDIR /opt  
RUN git clone git://github.com/opinkerfi/adagios.git  
WORKDIR /opt/adagios/adagios  
RUN cp -r etc/adagios /etc/adagios  
RUN chown -R nagios:nagios /etc/adagios  
RUN chmod g+w -R /etc/adagios  
RUN mkdir -p /var/lib/adagios/userdata  
RUN chown nagios:nagios /var/lib/adagios  
RUN mkdir /etc/nagios/adagios  
  
RUN mkdir -p /etc/nagios/adagios /etc/nagios/commands  
RUN echo "cfg_dir=/etc/nagios/adagios" >> /etc/nagios/nagios.cfg  
RUN echo "cfg_dir=/etc/nagios/commands" >> /etc/nagios/nagios.cfg  
RUN sed -i 's|debug_level=0|debug_level=1|g' /etc/nagios/nagios.cfg  
  
# Add naemon to apache group so it has permissions to pnp4nagios's session
files  
RUN usermod -G apache nagios  
  
RUN sed -i 's|^\\(nagios_init_script\\)=\\(.*\\)$|\1="sudo /usr/bin/nagios-
supervisor-wrapper.sh"|g' /etc/adagios/adagios.conf  
RUN echo "nagios ALL=NOPASSWD: /usr/bin/nagios-supervisor-wrapper.sh" >>
/etc/sudoers.d/adagios  
  
# Redirect / to /adagios  
RUN echo "RedirectMatch ^/$ /adagios" > /etc/httpd/conf.d/redirect.conf  
  
# Add supervisord conf, bootstrap.sh files  
ADD container-files /  
ADD supervisord-nagios.conf /etc/supervisor.d/supervisord-nagios.conf  
  
EXPOSE 80  
# Livestatus remote service  
EXPOSE 6557  
VOLUME ["/data", "/etc/nagios", "/var/log/nagios", "/etc/adagios",
"/opt/adagios", "/opt/pynag"]  
  
ENTRYPOINT ["/config/bootstrap.sh"]  

