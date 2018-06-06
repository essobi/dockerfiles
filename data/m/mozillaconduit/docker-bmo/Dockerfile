# This Source Code Form is subject to the terms of the Mozilla Public  
# License, v. 2.0. If a copy of the MPL was not distributed with this  
# file, You can obtain one at http://mozilla.org/MPL/2.0/.  
#  
# This Source Code Form is "Incompatible With Secondary Licenses", as  
# defined by the Mozilla Public License, v. 2.0.  
FROM mozillabteam/bmo-ci  
MAINTAINER David Lawrence <dkl@mozilla.com>  
  
ENV GIT_BASE_BRANCH master  
  
ENV CONDUIT_LOGIN conduit@mozilla.bugs  
ENV CONDUIT_PASSWORD password123456789!  
ENV CONDUIT_API_KEY zQ5TSBzq7tTZMtKYq9K1ZqJMjifKx3cPL7pIGk9Q  
  
ENV PHABRICATOR_LOGIN phab-bot@bmo.tld  
ENV PHABRICATOR_PASSWORD password123456789!  
ENV PHABRICATOR_API_KEY 8G4ly8JkxbypZgh5XrdiHWExVEjPq5S3HvMBll1K  
  
ENV BUGS_MYSQL_HOST localhost  
ENV BUGS_MYSQL_DBNAME bugs  
ENV BUGS_MYSQL_USER bugs  
ENV BUGS_MYSQL_PASSWORD bugs  
ENV MYSQL_ROOT_PASSWORD password  
  
# Distribution package installation  
COPY conf/rpm_list /  
RUN touch /var/lib/rpm/* \  
&& yum install -q -y yum-plugin-ovl \  
&& yum -q -y install `cat /rpm_list` \  
&& yum -q clean all  
  
# Sudoers setup  
COPY conf/sudoers /etc/sudoers  
RUN chown root.root /etc/sudoers && chmod 440 /etc/sudoers  
  
# Apache setup  
COPY conf/bugzilla.conf /etc/httpd/conf.d/bugzilla.conf  
RUN sed -e "s?^User apache?User $BUGZILLA_USER?" \--in-place
/etc/httpd/conf/httpd.conf  
RUN sed -e "s?^Group apache?Group $BUGZILLA_USER?" \--in-place
/etc/httpd/conf/httpd.conf  
  
# Postfix fix  
RUN sed -e "s?^inet_protocols = all?inet_protocols = ipv4?" \--in-place
/etc/postfix/main.cf  
  
# Development environment setup  
RUN rm -rf $BUGZILLA_ROOT \  
&& git clone $GITHUB_BASE_GIT -b $GITHUB_BASE_BRANCH $BUGZILLA_ROOT \  
&& ln -sf $BUGZILLA_LIB $BUGZILLA_ROOT/local  
COPY conf/checksetup_answers.txt $BUGZILLA_ROOT/checksetup_answers.txt  
  
# Copy and run setup scripts  
COPY scripts/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
RUN bugzilla_config.sh  
RUN su - $BUGZILLA_USER -c dev_config.sh  
  
RUN chown -R $BUGZILLA_USER.$BUGZILLA_USER $BUGZILLA_ROOT  
  
CMD ["entrypoint.sh"]  

