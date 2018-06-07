FROM sameersbn/redmine:2.6.6  
# for redmine http  
EXPOSE 80/tcp  
# for git ssh  
EXPOSE 22/tcp  
  
RUN apt-get update  
RUN apt-get install -y openssh-server build-essential libssh2-1 libssh2-1-dev
cmake libgpg-error-dev  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /  
COPY install_git_hosting.sh /  
RUN /install_git_hosting.sh  
  
# su redmine  
WORKDIR /home/redmine/redmine/plugins  
RUN sudo -HEu redmine git clone https://github.com/jbox-
web/redmine_bootstrap_kit.git &&\  
cd redmine_bootstrap_kit/ &&\  
git checkout 0.2.3  
  
RUN git clone https://github.com/jbox-web/redmine_git_hosting.git &&\  
cd redmine_git_hosting/ &&\  
git checkout 1.1.1  
  
# Before running bundle exec you must edit plugin’s Gemfile  
# (REDMINE_ROOT/plugin/redmine_git_hosting/Gemfile) and comment / uncomment
the  
# lines corresponding to your Redmine version (2.x or 3.x).  
RUN sed -i '/fix_rails4/d'
/home/redmine/redmine/plugins/redmine_git_hosting/Gemfile  
RUN sed -i '/3.1.2/d'
/home/redmine/redmine/plugins/redmine_git_hosting/Gemfile  
RUN sed -i '/dalli/d'
/home/redmine/redmine/plugins/redmine_git_hosting/Gemfile  
#RUN sed -i '/3.1.2/d' /home/redmine/redmine/Gemfile  
RUN echo "gem 'gitlab-grack', git: 'https://github.com/jbox-web/grack.git',
require: 'grack', branch: 'fix_rails3'" >>
/home/redmine/redmine/plugins/redmine_git_hosting/Gemfile  
RUN echo "gem 'redcarpet', '~> 2.3.0'" >>
/home/redmine/redmine/plugins/redmine_git_hosting/Gemfile  
  
RUN sudo -HEu redmine bundle install --without development test \--path
vendor/bundle  
  
#WORKDIR /home/redmine/redmine  
#RUN sudo -HEu redmine bundle install --without development test  
#RUN sudo -HEu redmine bundle exec rake redmine:plugins:migrate
RAILS_ENV=production NAME=redmine_git_hosting  
# install gitolite as user git  
RUN id  
RUN useradd -m git  
  
# - login to "git" on the server  
# - make sure your ssh public key from your workstation has been copied as
$HOME/YourName.pub  
WORKDIR /home/git  
RUN sudo -HEu git git clone git://github.com/sitaramc/gitolite
/home/git/gitolite  
RUN sudo -HEu git mkdir -p /home/git/bin  
RUN sudo -HEu git gitolite/install -to /home/git/bin  
  
# VOLUME  
VOLUME /home/git/repositories  
  
# config sudo:  
COPY redmine_sudoers /etc/sudoers.d/redmine  
RUN chmod 440 /etc/sudoers.d/redmine  
  
COPY entrypoint_gitolite.sh /sbin/  
RUN chmod 755 /sbin/entrypoint_gitolite.sh  
ENTRYPOINT ["/sbin/entrypoint_gitolite.sh"]  
CMD ["app:start"]  

