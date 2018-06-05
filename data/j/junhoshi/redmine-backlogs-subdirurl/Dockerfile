FROM library/ubuntu:14.04.3  
MAINTAINER 74th<site@j74th.com>  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN echo "mysql-server-5.5 mysql-server/root_password password redmine" |
debconf-set-selections  
RUN echo "mysql-server-5.5 mysql-server/root_password_again password redmine"
| debconf-set-selections  
RUN apt-get install -y \  
build-essential zlib1g-dev libssl-dev libreadline-dev libyaml-dev
libcurl4-openssl-dev \  
mysql-server-5.5 \  
apache2-mpm-worker apache2-threaded-dev libapr1-dev libaprutil1-dev
apache2-utils \  
imagemagick libmagick++-dev fonts-takao-pgothic \  
subversion libapache2-svn \  
git gitweb libssh2-1 libssh2-1-dev cmake libgpg-error-dev \  
ruby2.2 ruby2.2-dev \  
libapache2-mod-auth-mysql libdigest-sha-perl libapache-dbi-perl libdbd-mysql-
perl libauthen-simple-ldap-perl  
  
RUN gem install bundler  
RUN gem install passenger --no-rdoc --no-ri  
RUN passenger-install-apache2-module \--auto  
# Redmine  
RUN svn co http://svn.redmine.org/redmine/branches/3.2-stable/
/var/lib/redmine  
ADD config/* /var/lib/redmine/config/  
WORKDIR /var/lib/redmine  
# redmine backlogs  
RUN git clone -b feature/redmine3
https://github.com/backlogs/redmine_backlogs.git
/var/lib/redmine/plugins/redmine_backlogs  
RUN sed -i -e 's/gem "nokogiri".*/gem "nokogiri", ">= 1.6.7.2"/g'
/var/lib/redmine/plugins/redmine_backlogs/Gemfile  
RUN sed -i -e 's/gem "capybara", "~> 1"//g'
/var/lib/redmine/plugins/redmine_backlogs/Gemfile  
# scm creator  
RUN git clone https://github.com/ZIMK/scm-creator.git
/var/lib/redmine/plugins/redmine_scm  
ADD scm-post-create.sh /var/lib/redmine/  
# issue template  
RUN apt-get install -y mercurial  
RUN hg clone https://bitbucket.org/akiko_pusu/redmine_issue_templates
/var/lib/redmine/plugins/redmine_issue_templates  
# code review  
RUN hg clone https://bitbucket.org/haru_iida/redmine_code_review
/var/lib/redmine/plugins/redmine_code_review  
# clipboard_image_paste  
RUN git clone https://github.com/peclik/clipboard_image_paste.git
/var/lib/redmine/plugins/clipboard_image_paste  
  
# excel export  
RUN git clone https://github.com/two-pack/redmine_xls_export.git
/var/lib/redmine/plugins/redmine_xls_export  
RUN sed -i -e 's/gem "nokogiri".*/gem "nokogiri", ">= 1.6.7.2"/g'
/var/lib/redmine/plugins/redmine_xls_export/Gemfile  
# drafts  
RUN git clone https://github.com/jbbarth/redmine_drafts.git
/var/lib/redmine/plugins/redmine_drafts  
  
# bundle and rake  
RUN bundle install --without development test --path vendor/bundle  
RUN bundle exec gem install mysql  
RUN chown -R www-data:www-data /var/lib/redmine/  
ADD redmine/Makefile /var/lib/redmine/  
RUN make rake  
  
# apache2  
ADD apache2/conf-available/redmine.conf /etc/apache2/conf-available/  
ADD apache2/mods-available/dav_svn.conf /etc/apache2/mods-available/  
ADD apache2/sites-available/000-default.conf /etc/apache2/sites-available/  
# use Redmine Auth  
RUN mkdir -p /etc/perl/Apache/Authn  
RUN cp /var/lib/redmine/extra/svn/Redmine.pm /etc/perl/Apache/Authn/Redmine.pm  
  
RUN passenger-install-apache2-module \--snippet >> /etc/apache2/conf-
available/redmine.conf  
RUN a2enconf redmine  
RUN a2enmod cgi alias env  
  
# repository  
RUN mkdir /var/lib/svn/  
RUN chown -R www-data:www-data /var/lib/svn/ /var/lib/git/  
# synbolicLink  
RUN ln -s /var/lib/redmine/public /var/www/html/redmine  
# ginalize  
EXPOSE 80  
ADD entrypoint.sh /root/  
ENTRYPOINT sh /root/entrypoint.sh  

