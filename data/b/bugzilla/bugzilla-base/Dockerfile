# This Source Code Form is subject to the terms of the Mozilla Public  
# License, v. 2.0. If a copy of the MPL was not distributed with this  
# file, You can obtain one at http://mozilla.org/MPL/2.0/.  
#  
# This Source Code Form is "Incompatible With Secondary Licenses", as  
# defined by the Mozilla Public License, v. 2.0.  
FROM centos:7  
MAINTAINER David Lawrence <dkl@mozilla.com>  
  
# Environment configuration  
ENV BUGZILLA_LIB /opt/bugzilla  
ENV BUGZILLA_WWW /var/www/html/bugzilla  
ENV GITHUB_BASE_GIT https://github.com/bugzilla/bugzilla  
ENV GITHUB_BASE_BRANCH master  
  
ADD https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
/usr/local/bin/cpanm  
RUN chmod 755 /usr/local/bin/cpanm  
  
COPY rpm_list /rpm_list  
RUN rpm -qa --queryformat '/^%{NAME}$/ d\n' > rpm_fix.sed && \  
sed -f rpm_fix.sed /rpm_list > /rpm_list.clean  
  
RUN yum -y -q install https://dev.mysql.com/get/mysql-community-release-
el7-5.noarch.rpm && \  
yum -y -q install epel-release && \  
yum -y -q install `cat /rpm_list.clean` && \  
yum clean all  
  
RUN pip install --upgrade pip rst2pdf sphinx  
  
# Clone the code repo and install dependencies  
ENV INSTALL_CPANM "cpanm -l $BUGZILLA_LIB --quiet --skip-satisfied --notest"  
RUN git clone $GITHUB_BASE_GIT -b master $BUGZILLA_WWW && \  
cd $BUGZILLA_WWW && \  
$INSTALL_CPANM HTML::Formatter && \  
$INSTALL_CPANM \--installdeps --with-all-features --with-recommends --without-
feature oracle . && \  
cd / && \  
rm -rf $BUGZILLA_WWW ~/.cpanm  
RUN git clone $GITHUB_BASE_GIT -b 5.0 $BUGZILLA_WWW && \  
cd $BUGZILLA_WWW && \  
$INSTALL_CPANM \--installdeps --with-all-features --with-recommends --without-
feature oracle . && \  
cd / && \  
rm -rf $BUGZILLA_WWW ~/.cpanm  
RUN git clone $GITHUB_BASE_GIT -b 4.4 $BUGZILLA_WWW && \  
cd $BUGZILLA_WWW && \  
$INSTALL_CPANM \--installdeps --with-all-features --with-recommends --without-
feature oracle . && \  
cd / && \  
rm -rf $BUGZILLA_WWW ~/.cpanm  

