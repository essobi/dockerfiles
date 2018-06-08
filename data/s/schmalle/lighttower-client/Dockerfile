#  
# docker build file for Lighttower Scanner  
#  
FROM honeynet/thug  
  
MAINTAINER Markus Schmall  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN mkdir /data  
RUN apt-get -y install nmap git gem skipfish build-essential git-core curl
zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev
libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-
software-properties libffi-dev curl libcurl4-openssl-dev  
  
RUN mkdir /scanner  
  
ADD ./executor.py /scanner/executor.py  
ADD ./start.sh /scanner/start.sh  
ADD ./thugcanvasscan.py /scanner/thugcanvasscan.py  
  
RUN cd /scanner && git clone https://github.com/nabla-c0d3/sslyze.git  
  
RUN apt-get install -y wget unzip openssl libreadline6 libreadline6-dev curl
zlib1g libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf
libc6-dev ncurses-dev automake libtool bison subversion pkg-config  
  
# Install rbenv to install ruby  
RUN git clone git://github.com/sstephenson/rbenv.git /usr/local/rbenv  
RUN echo '# rbenv setup' > /etc/profile.d/rbenv.sh  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh  
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
RUN chmod +x /etc/profile.d/rbenv.sh  
  
# Install rbenv plugin: ruby-build  
RUN mkdir /usr/local/rbenv/plugins  
RUN git clone https://github.com/sstephenson/ruby-build.git
/usr/local/rbenv/plugins/ruby-build  
  
# Let's not copy gem package documentation  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
ENV RBENV_ROOT /usr/local/rbenv  
ENV PATH
$RBENV_ROOT/bin:$RBENV_ROOT/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/arachni-1.4-0.5.10/bin  
  
# Install ruby  
RUN rbenv install 2.2.4  
RUN rbenv local 2.2.4  
RUN rbenv global 2.2.4  
  
RUN cd /scanner  
RUN wget
https://github.com/Arachni/arachni/releases/download/v1.4/arachni-1.4-0.5.10-linux-x86_64.tar.gz  
RUN tar -xzvf arachni-1.4-0.5.10-linux-x86_64.tar.gz  
  
RUN rbenv rehash  
  
CMD ["/bin/bash"]  
  

