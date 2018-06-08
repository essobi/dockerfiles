FROM ubuntu  
MAINTAINER Rodney Persky <rodney.persky@gmail.com>  
  
  
  
# Refresh the package list  
RUN export version=$(cat /etc/lsb-release | grep DISTRIB_CODENAME=precise |
cut -d '=' -f2) && \  
echo deb http://archive.ubuntu.com/ubuntu $version universe >>
/etc/apt/sources.list && \  
echo deb http://archive.canonical.com/ $version partner >>
/etc/apt/sources.list && \  
apt-get update  
  
# To download SCM For Mercurial Plugin  
# Install | Mercurial SVN |  
# | | | |  
RUN apt-get install -y wget openjdk-7-jre-headless mercurial git subversion
python2.7  
# | | |  
# To run SCM GIT SVN  
# Install the program in one big step  
RUN mkdir /usr/share/scm-manager && \  
cd /usr/share/scm-manager && \  
wget https://repository-scm-
manager.forge.cloudbees.com/snapshot/sonia/scm/scm-server/1.36-SNAPSHOT/scm-
server-1.36-20131230.140542-1-app.tar.gz && \  
tar -xzf $(ls | grep ".gz") && \  
rm $(ls | grep ".gz")  
  
# Note I suggest to use /datay as the location where the repository files can
be kept  
# as then you can use -b /home/repos:/data to bind the two filesystems
together  
# | |  
# | SCM server  
# On your computer  
# It is then easy to progress and import your own repositories following the
scm layout of  
# data/hg <\- storage of mercurial repositories  
# git <\- storage of git repositories  
# svn <\- storage of subversion repositories  
EXPOSE 8080  
CMD ["/usr/share/scm-manager/scm-server/bin/scm-server"]  
VOLUME ["/data"]  

