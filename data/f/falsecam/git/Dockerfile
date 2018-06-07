FROM debian:8.1  
RUN apt-get -y update  
RUN apt-get -y install apache2 openssh-server git subversion libapache2-svn  
  
RUN service apache2 start  
RUN mkdir /var/run/sshd  
  
RUN adduser --system git  
RUN mkdir -p /home/git/.ssh && mkdir -p /repos && mkdir -p /svn-repos/repo  
RUN echo 'git:password' | chpasswd  
  
RUN a2enmod authz_user && a2enmod dav && a2enmod dav_svn && a2enmod authz_svn  
RUN svnadmin create /svn-repos/repo  
RUN chown -R www-data /svn-repos  
RUN htpasswd -cmb /etc/apache2/dav_svn.passwd user changeme  
  
RUN sed -i s#/home/git:/bin/false#/home/git:/bin/bash# /etc/passwd  
  
COPY dav_svn.conf /etc/apache2/mods-available/dav_svn.conf  
COPY dav_svn.authz /etc/apache2/dav_svn.authz  
  
RUN service apache2 restart  
  
EXPOSE 22 80  
CMD ["/usr/sbin/sshd", "-D"]  

