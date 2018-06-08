FROM tuxmonteiro/centos6-dev  
  
MAINTAINER marcelotmonteiro@nospam.com  
  
WORKDIR /root  
  
USER root  
  
ENV RUBY_VER 2.1.2  
ENV GITLAB_BRANCH 8-10-stable  
  
COPY patches /root/patches  
  
RUN echo "Starting..."; \  
git clone -b ${GITLAB_BRANCH} https://github.com/gitlabhq/omnibus-gitlab.git
/root/omnibus-gitlab; \  
mkdir -p /root/omnibus-gitlab/pkg; \  
cd /root/omnibus-gitlab; \  
for p in /root/patches/*patch; do patch -p1 < $p; done; \  
source /root/.bash_profile; \  
bundle install --path=.bundle --binstubs; \  
sed -i "s%XXXX%$(ls -d /root/omnibus-
gitlab/.bundle/ruby/*/bundler/gems/omnibus-* | grep -v software | sed
's|/root/omnibus-gitlab/.bundle/ruby/.*/bundler/gems/omnibus-||')%"
/root/patches/post/health_check.rb-whitelist.patch; \  
sed -i "s%YYYY%$(ls -d /root/omnibus-
gitlab/.bundle/ruby/*/bundler/gems/omnibus-software-* | sed 's|/root/omnibus-
gitlab/.bundle/ruby/.*/bundler/gems/omnibus-software-||')%"
/root/patches/post/fix-runsvdir-start.erb.patch; \  
patch -p1 < /root/patches/post/health_check.rb-whitelist.patch; \  
patch -p1 < /root/patches/post/fix-runsvdir-start.erb.patch; \  
echo "Finished."  
  
WORKDIR /root/omnibus-gitlab  
  
VOLUME ["/var/cache/omnibus", "/root/omnibus-gitlab/pkg"]  
  
ENTRYPOINT ["/bin/su", "-l", "root", "-c"]  

