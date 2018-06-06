FROM debian:8.2  
MAINTAINER Baptiste Mathus <batmat@batmat.net>  
  
RUN apt-get update -y && \  
apt-get install -y \  
subversion \  
curl \  
bzip2 \  
git \  
git-svn && \  
apt-get clean  
  
ENV MOJOHAUS_SVN_REPO mojohaus-svn-repo  
  
# Get the SVN Dump and show this is the same content posted months ago  
# (i.e. nothing malicious introduced *in the meantime* or something)  
# Cf. https://groups.google.com/forum/#!topic/mojohaus-dev/DdGVMUVykhU for
reference  
# TODO : host it somewhere more durable, maybe Bintray? Central?  
RUN curl https://dl.dropboxusercontent.com/u/6790263/mojo-scm-20150517.bz2 >
svndump.bz2 && \  
echo 35187dcfb204c5ab14ec9155ed303c90 svndump.bz2 | md5sum -c --status - && \  
svnadmin create $MOJOHAUS_SVN_REPO && \  
bunzip2 svndump.bz2 --stdout | svnadmin load $MOJOHAUS_SVN_REPO \--bypass-
prop-validation && \  
rm svndump.bz2  
  
# OK, now we have the svn repository fully loaded, we can work on it  
RUN mkdir /newgitrepo  
WORKDIR /newgitrepo  
  
ADD migration-tools /migration-tools  
  
CMD ["/migration-tools/convert-project.sh"]  

