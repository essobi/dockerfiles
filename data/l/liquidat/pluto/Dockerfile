# Pluto planet feedreader  
#  
FROM centos:latest  
  
RUN yum install -y epel-release centos-release-scl && yum install -y rh-ruby23
gcc make sqlite-devel nginx rh-ruby23-ruby-devel && yum clean all  
RUN scl enable rh-ruby23 -- gem install activerecord  
RUN scl enable rh-ruby23 -- gem install sqlite3  
RUN scl enable rh-ruby23 -- gem install pluto  
RUN scl enable rh-ruby23 -- pluto i blank  
  
# prepare data directory for ini file, copy basic ini file  
RUN mkdir /data/  
ADD planet.ini /data/planet.ini  
  
# copy starter script  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# patch blank template to contain feeds  
ADD atom.xml.erb /root/.pluto/blank/atom.xml.erb  
ADD rss.xml.erb /root/.pluto/blank/rss.xml.erb  
ADD blank.html.erb /root/.pluto/blank/blank.html.erb  
ADD blank.txt /root/.pluto/blank/blank.txt  
  
ENTRYPOINT ["/bin/sh","-c","/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 80  

