FROM sameersbn/redmine:2.6.6-1  
MAINTAINER FayeHuang  
  
WORKDIR /home/redmine/redmine  
  
RUN apt-get update -y && \  
apt-get install -y vim unzip ruby ruby-dev cpp gcc libxml2 libxml2-dev
libxslt1-dev && \  
apt-get clean all  
RUN bundle install --without development test  
RUN gem install holidays --version 1.0.3 && gem install holidays  
  
# http://www.redminecrm.com/projects/checklist/wiki  
COPY redmine_checklists-3_1_3-light.zip
/tmp/redmine_checklists-3_1_3-light.zip  
RUN unzip /tmp/redmine_checklists-3_1_3-light.zip -d ./plugins  
  
# http://www.redminebacklogs.net/en/installation.html  
RUN git clone \--branch v1.0.6 https://github.com/backlogs/redmine_backlogs
./plugins/redmine_backlogs  
  
# https://github.com/makotokw/redmine-theme-gitmike  
RUN git clone git://github.com/makotokw/redmine-theme-gitmike.git
./public/themes/gitmike  
  
RUN bundle update nokogiri && bundle install  
  
COPY plugins_init.sh ./plugins_init.sh  
RUN chmod +x ./plugins_init.sh  

