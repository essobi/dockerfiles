FROM helioncf/base  
  
RUN add-apt-repository --yes ppa:brightbox/ruby-ng && \  
apt-get update && apt-get install -y \  
# required for ruby packages  
# determined from https://gorails.com/setup/ubuntu/14.04  
git-core \  
build-essential \  
libcurl4-openssl-dev \  
libffi-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
sqlite3 \  
zlib1g-dev \  
# end of ruby requireds.  
# required for bright box ruby and python  
software-properties-common \  
# required python and nodejs dependencies  
curl \  
# required for nodejs  
apt-transport-https \  
#ruby core packages from BrightBox  
ruby-switch \  
ruby2.1 \  
ruby2.1-dev \  
ruby2.1-doc && \  
#end core ruby packages from BrightBox  
gem install bundler  
  
# Attempted to put python install in with all components above  
# but got this error, "python: can't open file 'python-dev': [Errno 2] No such
file or directory"  
# also to install node there is a curl dependency for node so it seems there
needs to be multiple apt-get installs anyway.  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& echo 'deb https://deb.nodesource.com/node_4.x trusty main' >
/etc/apt/sources.list.d/nodesource.list && \  
#add repos for python  
add-apt-repository --yes ppa:fkrull/deadsnakes-python2.7 && \  
add-apt-repository --yes ppa:fkrull/deadsnakes && apt-get update && apt-get
install -y \  
python \  
python-dev \  
python3.5 \  
python3.5-dev \  
# run commands to install nodejs  
nodejs && \  
#install pip for both versions of python  
curl --silent https://raw.githubusercontent.com/pypa/pip/master/contrib/get-
pip.py | python3 && \  
curl --silent https://raw.githubusercontent.com/pypa/pip/master/contrib/get-
pip.py | python2 && \  
ln -sf `which python3.5` `which python3` && \  
# step is made for installing Ruby gems, doing this here to remove a run layer
command  
mkdir sentinel  
  
# Add sentinel gems  
COPY ./sentinel ./sentinel  
RUN cd sentinel/cli && bundle install && cd .. && cd daemon && bundle install  

