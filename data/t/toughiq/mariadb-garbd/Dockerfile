FROM centos:7  
MAINTAINER toughIQ <toughiq@gmail.com>  
  
ADD MariaDB.repo /etc/yum.repos.d/  
  
RUN yum update -y \  
&& rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB \  
&& yum install -y MariaDB-server \  
&& yum clean all  
  
ENTRYPOINT ["/bin/garbd"]  
  
CMD ["--help"]

