FROM centos:7  
ENV MAXSCALE_PACKAGE_VERSION=2.2.5-1  
RUN yum install -y epel-release  
RUN yum install -y
https://downloads.mariadb.com/MaxScale/latest/rhel/7/x86_64/maxscale-${MAXSCALE_PACKAGE_VERSION}.rhel.7.x86_64.rpm  
RUN mkdir -p /tmp/maxadmin  
CMD ["maxscale", "-f", "/etc/maxscale.cnf", "-l", "stdout", "-d", "-U",
"root"]  

