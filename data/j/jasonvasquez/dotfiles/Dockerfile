FROM ubuntu:wily  
MAINTAINER jason@mugfu.com  
  
ENV USER="jvasquez"  
ENV EMAIL="jason@mugfu.com"  
ENV FULLNAME="Jason Vasquez"  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
# Packages ==============================================  
RUN apt-get -y install \  
build-essential \  
curl \  
git \  
git-flow \  
libcurl4-openssl-dev \  
libffi-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
openjdk-8-jdk \  
python-software-properties \  
silversearcher-ag \  
sqlite3 \  
vim \  
wget \  
zlib1g-dev \  
zsh  
  
# User Account ==============================================  
RUN useradd -m -s /bin/zsh jvasquez  
WORKDIR /home/jvasquez  
USER jvasquez  
  
# git lfs ==============================================  
USER root  
RUN \  
mkdir t && \  
cd t && \  
curl --silent -LO https://github.com/github/git-
lfs/releases/download/v1.0.2/git-lfs-linux-amd64-1.0.2.tar.gz && \  
tar xzf git-lfs-linux-amd64-1.0.2.tar.gz && \  
cd git-lfs-1.0.2 && \  
./install.sh && \  
cd /home/jvasquez && \  
rm -rf /home/jvasquez/t  
USER jvasquez  
  
  
# ohmyzsh ==============================================  
# Adding 'true' to the end, this thing exits non-zero for some reason even
when it works  
RUN sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"; true  
  
# Ruby dev environment ==============================================  
# (based on https://gorails.com/setup/ubuntu/15.10)  
RUN \  
git clone git://github.com/sstephenson/rbenv.git .rbenv && \  
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc && \  
echo 'eval "$(rbenv init -)"' >> ~/.zshrc && \  
\  
git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-
build && \  
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.zshrc &&
\  
\  
git clone https://github.com/sstephenson/rbenv-gem-rehash.git
~/.rbenv/plugins/rbenv-gem-rehash && \  
\  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
RUN /bin/zsh --interactive -c 'rbenv install 2.2.3'  
RUN /bin/zsh --interactive -c 'rbenv global 2.2.3'  
RUN /bin/zsh --interactive -c 'gem install bundler'  
  
# Node dev environment ==========================================  
# (based around nodenv)  
RUN \  
git clone https://github.com/OiNutter/nodenv.git ~/.nodenv && \  
echo 'export PATH="$HOME/.nodenv/bin:$PATH"' >> ~/.zshrc && \  
echo 'eval "$(nodenv init -)"' >> ~/.zshrc  
  
RUN /bin/zsh --interactive -c 'git clone https://github.com/OiNutter/node-
build.git $(nodenv root)/plugins/node-build'  
RUN /bin/zsh --interactive -c 'nodenv install 4.2.2'  
RUN /bin/zsh --interactive -c 'nodenv global 4.2.2'  
  
# sudo support ===================================================  
USER root  
RUN apt-get -y install sudo  
RUN echo "jvasquez ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
USER jvasquez  
  
# got the basics out of the way, add in zsh script loading ========  
RUN \  
mkdir ~/.zsh.d && \  
echo "for file in ~/.zsh.d/*.zsh; do" >> ~/.zshrc && \  
echo ' source "$file"' >> ~/.zshrc && \  
echo "done" >> ~/.zshrc  
  
# a mountpoint for persistent data ================================  
RUN mkdir /home/jvasquez/mnt  
VOLUME /home/jvasquez/mnt  
  
# Just mount in .ssh (and its keys) from the host for ease ========  
VOLUME /home/jvasquez/.ssh  
  
# The actual dotfiles =============================================  
ADD . /home/jvasquez  
USER root  
RUN chown -R jvasquez:jvasquez /home/jvasquez  
  
USER jvasquez  

