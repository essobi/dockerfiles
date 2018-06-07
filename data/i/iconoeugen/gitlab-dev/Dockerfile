FROM iconoeugen/ruby-dev:latest  
MAINTAINER info@vlad.eu  
  
# install things globally, for great justice  
# Default: https://gitlab.com/gitlab-org/gitlab-ce.git  
ENV gitlab_repo ""  
# Default: https://gitlab.com/gitlab-org/gitlab-shell.git  
ENV gitlab_shell_repo ""  
# Default: https://gitlab.com/gitlab-org/gitlab-workhorse.git  
ENV gitlab_workhorse_repo ""  
# Default: https://gitlab.com/gitlab-org/gitlab-development-kit.git  
ENV gitlab_development_kit_repo ""  
COPY yarn.repo /etc/yum.repos.d/  
  
RUN dnf -y install postgresql libpqxx-devel postgresql-libs redis libicu-devel
nodejs git ed cmake rpm-build gcc-c++ yarn krb5-devel go postgresql-server
postgresql-contrib zlib-devel \  
&& dnf clean all  
  
ENV PHANTOMJS_VERSION 2.1.1  
RUN curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2
| tar -xjC /tmp \  
&& mv /tmp/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs /usr/bin/
\  
&& rm -rf /tmp/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64  
  
RUN ln -s /workspace/gitlab-development-kit /home/git  
  
COPY gdk-init.sh /etc/profile.d/gdk-init.sh  
  
EXPOSE 3000  
CMD [ "/bin/bash" ]

