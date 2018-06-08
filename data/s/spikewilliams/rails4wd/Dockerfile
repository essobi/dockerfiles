FROM fedora  
MAINTAINER Bobby Williams spikewilliams@gmail.com @spike@mastodon.al  
  
RUN dnf -y install git gcc make bzip2 openssl-devel readline-devel zlib-devel
\  
sqlite-devel gcc-c++ wget sudo curl which autoconf fontconfig \  
htop procps-ng \  
libxml2 libxml2-devel libxslt libxslt-devel \  
findutils file ImageMagick nodejs  
  
RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv \  
&& cd ~/.rbenv \  
&& src/configure \  
&& make -C src  
  
RUN git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-
build  
  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc  
  
#add heroku support  
#RUN wget -qO- https://toolbelt.heroku.com/install.sh | sh  
#add phantomjs support  
#RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
# && bzip2 -dc phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar x \  
# && cd phantomjs-2.1.1-linux-x86_64 \  
# && mv bin/phantomjs /usr/bin  
VOLUME ["/railsapp"]  
COPY rootfs /  
  
EXPOSE 3000  

