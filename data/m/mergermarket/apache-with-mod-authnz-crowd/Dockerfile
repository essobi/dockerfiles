# centos 5 support until Mar 31st, 2017. Using this old distro as  
# there are currently few options
(https://confluence.atlassian.com/display/CROWD/Integrating+Crowd+with+Apache)  
# Hopefully the pull requests here https://bitbucket.org/atlassian/cwdapache
should be integrated in time to upgrade  
FROM centos:6  
COPY mod_authnz_crowd-2.2.2-1.el6.x86_64.rpm /tmp/  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
  
RUN yum upgrade -y && \  
echo $'update\n localinstall /tmp/mod_authnz_crowd-2.2.2-1.el6.x86_64.rpm\n ts
run\n' | yum shell -y --nogpgcheck  
  
# this module doesn't work (undefined symbols)  
RUN rm -f /etc/httpd/conf.d/subversion.conf  
  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-D", "FOREGROUND"]  

