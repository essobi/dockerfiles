FROM debian:wheezy  
MAINTAINER Christian Simon <simon@swine.de>  
  
# Install requirements  
ADD sources.list /etc/apt/sources.list  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install subversion wget svn-
buildpackage nginx-full && \  
DEBIAN_FRONTEND=noninteractive apt-get -y build-dep openssl && \  
apt-get clean && \  
rm /var/lib/apt/lists/*_*  
  
# Download, build and install a vulnerable openssl  
RUN mkdir /tmp/openssl-heartbleed && \  
mkdir /tmp/openssl-heartbleed/tarballs && \  
wget
http://ftp.debian.org/debian/pool/main/o/openssl/openssl_1.0.1e.orig.tar.gz -O
/tmp/openssl-heartbleed/tarballs/openssl_1.0.1e.orig.tar.gz && \  
svn co svn://anonscm.debian.org/svn/pkg-openssl/openssl/tags/1.0.1e-2+deb7u4/
/tmp/openssl-heartbleed/openssl && \  
cd /tmp/openssl-heartbleed/openssl && \  
svn-buildpackage && \  
dpkg -i /tmp/openssl-heartbleed/build-area/openssl_1.0.1e-2+deb7u4_amd64.deb
/tmp/openssl-heartbleed/build-area/libssl1.0.0_1.0.1e-2+deb7u4_amd64.deb && \  
rm -rf /tmp/openssl-heartbleed  
  
# Copy nginx ssl configuration  
ADD nginx.conf /etc/nginx/sites-available/default  
  
# Add starting script  
ADD run.sh /run.sh  
  
CMD /run.sh  
EXPOSE 443  

