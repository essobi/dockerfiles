FROM bitnami/apache:latest  
  
MAINTAINER True Stealth <admin@infostore.ru>  
  
RUN install_packages mc libdbd-mysql-perl libapache2-mod-perl2 libapache-dbi-
perl  
RUN bitnami-pkg install git-2.14.2-0 --checksum
3fa698364678e696e0b580cd7e9979a453ad5c590c373dbe5217cdcbd3666ec9  
  
RUN curl -sSL
https://raw.githubusercontent.com/redmine/redmine/master/extra/svn/Redmine.pm
> /usr/share/perl5/Apache/Redmine.pm  
  
ENV PATH="/opt/bitnami/git/bin:$PATH"  
EXPOSE 3000

