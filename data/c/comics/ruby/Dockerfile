FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: ruby  
# Software Version: 2.3.1  
# Software Website:  
# Description: ruby  
##############################################################  
  
ENV APP_NAME=ruby  
ENV VERSION=2.3.1  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION/bin:$PATH  
ENV MANPATH=$DEST/$VERSION/share/man:$MANPATH  
  
RUN yum install -y zlib zlib-devel openssl openssl-devel readline readline-
devel ; \  
yum clean all ; \  
curl -L -o $APP_NAME-$VERSION.tar.gz https://cache.ruby-
lang.org/pub/ruby/2.3/$APP_NAME-$VERSION.tar.gz ; \  
tar xvf $APP_NAME-$VERSION.tar.gz ; \  
cd $APP_NAME-$VERSION ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp COPYING /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
./configure --prefix=$DEST/$VERSION ; \  
make ; \  
make install ; \  
cd ../ ; \  
rm -rf $APP_NAME-$VERSION $APP_NAME-$VERSION.tar.gz  
CMD ["/bin/bash"]  
  

