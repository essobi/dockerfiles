FROM tsweb/node:4  
MAINTAINER Kazuhisa Kumagai <k-kumagai@ts.tv-osaka.co.jp>  
  
#--------------------------------------  
# update Git  
#--------------------------------------  
RUN yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-
devel perl-ExtUtils-MakeMaker | true  
RUN yum -y remove git  
  
RUN (\  
cd /usr/local/src;\  
yum -y install wget tar gcc;\  
wget -O git.tar.gz
https://www.kernel.org/pub/software/scm/git/git-2.7.3.tar.gz;\  
tar zxvf git.tar.gz;\  
cd git-2.7.3;\  
./configure \  
\--prefix=/usr/local;\  
make prefix=/usr/local all;\  
make prefix=/usr/local install;\  
)  
  
#--------------------------------------  
# install Bower  
#--------------------------------------  
RUN npm install -g bower  
  
# https://github.com/angular/angular-phonecat/issues/141  
RUN git config --system url."https://".insteadOf git://  
  
#--------------------------------------  
# install Yeoman  
#--------------------------------------  
RUN npm install -g yo  
RUN npm install -g "git+https://bitbucket.org/tvoweb2/yeoman-generator-tvo-
html.git"  
  
#--------------------------------------  
# install ungit  
#--------------------------------------  
RUN npm install -g ungit  
  
#--------------------------------------  
# initialize  
#--------------------------------------  
ADD supervisor.conf /etc/supervisord/conf/service.conf  
  
ADD id_rsa.pub /id_rsa.pub  
  
#--------------------------------------  
# run  
#--------------------------------------  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

