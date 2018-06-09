FROM ubuntu:14.04  
MAINTAINER thaim <thaim24@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
subversion \  
apache2 \  
apache2-utils \  
libapache2-svn \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN mkdir -p /home/svn/SampleProject \  
&& groupadd subversion \  
&& usermod -G subversion www-data \  
&& usermod -G subversion root \  
&& svnadmin create /home/svn/SampleProject \  
&& chown -R www-data:subversion /home/svn/SampleProject \  
&& chmod -R g+rws /home/svn/SampleProject \  
&& htpasswd -cb /etc/subversion/passwd user password  
  
COPY dav_svn.conf /etc/apache2/mods-available/  
COPY apache2.conf /etc/apache2/  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME ["/home/svn"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

