FROM project42/centos-apache  
# FROM local/apache  
MAINTAINER Brandon Cone bcone@esu10.org  
  
# Set up a wordpress instantiation. This is independent of a webserver, etc,
even though it  
# inherets from it because we want these to be standalone.  
  
ENV WP_VERSION 4.8.2  
ENV WP_MD5 2e8744a702a3d9527782d9135a4c9544  
# ENV WP_VERSION 4.9.4  
# ENV WP_MD5 ff84abd9ec38b93ef0ea09b05e85467b  
  
RUN yum install -y php56w-mysqlnd git mailx ssmtp && \  
# RUN yum install -y php56w-mysqlnd git && \  
cd /tmp && \  
wget --quiet https://wordpress.org/wordpress-${WP_VERSION}.tar.gz && \  
echo "$WP_MD5 *wordpress-$WP_VERSION.tar.gz" | md5sum -c - && \  
tar xzf wordpress-${WP_VERSION}.tar.gz -C /var/www/html/ && \  
rm -f wordpress-${WP_VERSION} && \  
mkdir /var/keep && \  
# Because of how volumes are mounted, volumes will "hide" what was downloaded  
# so we copy out as part of setting persistence.  
# This process completes in our install-wordpress.sh file.  
cp -r /var/www/html/wordpress/wp-content/* /var/keep/ && \  
  
# wget --quiet https://downloads.wordpress.org/theme/school.1.4.5.zip && \  
########################  
# Install the WP Shell #  
########################  
# curl -O --silent https://raw.githubusercontent.com/wp-cli/builds/gh-
pages/phar/wp-cli.phar && \  
# chmod +x wp-cli.phar && \  
# mv wp-cli.phar /usr/local/bin/wpsh && \  
# # tar xzf school.1.4.5.zip -C /var/keep/themes/ && \  
# # rm school.1.4.5.zip && \  
# echo "Contents of keep directory" && \  
# ls /var/keep && \  
yum -y clean all  
  
COPY container-files /

