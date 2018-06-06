FROM ubuntu:12.04.5  
MAINTAINER Chris Ortman <chrisortman@gmail.com>  
  
# install the prerequisite patches here so that rvm will install under non-
root account.  
# I listed cups and freetds / odbc first since those were the ones that gave
me  
# the most headache in regard to package dependencies  
# I figure this way they get first say in what version of what gets installed
so  
# hopefully fewer conflicts  
RUN apt-get update && apt-get install --assume-yes cups libcups2-dev \  
freetds-dev freetds-bin tdsodbc \  
unixodbc unixodbc-dev \  
openssh-server git-core openssh-client curl vim \  
build-essential \  
openssl libreadline6 libreadline6-dev curl \  
zlib1g zlib1g-dev libssl-dev libyaml-dev \  
libsqlite3-dev sqlite3 libxml2-dev libxslt-dev \  
autoconf libc6-dev ncurses-dev automake \  
strace \  
libtool bison pkg-config gawk libgdbm-dev libffi-dev nodejs  
  
#------------------ FIREFOX ------------------------  
RUN apt-get update && apt-get install -y xfonts-100dpi xfonts-75dpi xfonts-
scalable \  
xfonts-cyrillic xvfb x11-apps imagemagick \  
libasound2 libgtk2.0-dev  
  
RUN mkdir -p /tmp  
  
# I can either add straight from the URL  
# and then unpack on the server  
# or I can download the archive and add that and  
# it will be extracted for me  
# ADD
https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest-24.0esr/linux-x86_64/en-
US/firefox-24.8.1esr.tar.bz2 /opt/  
ADD
https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/38.1.0esr/linux-x86_64/en-
US/firefox-38.1.0esr.tar.bz2 /opt/firefox.tar.bz2  
RUN cd /opt && tar -vxjf firefox.tar.bz2 && rm firefox.tar.bz2 && cd /  
RUN ln -s /opt/firefox/firefox /usr/bin/firefox  
  
# Export display variable for communication between xvfb and firefox  
ENV DISPLAY :99  
#------------------------------------------------------  
ADD scripts/xvfb /etc/init.d/xvfb  
# make sure we get right timezone  
RUN echo America/Chicago > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN useradd -ms /bin/bash appuser  
USER appuser  
  
# install rvm with ruby 1.9.3  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN \curl -L get.rvm.io | bash -s stable --autolibs=read-fail  
RUN /bin/bash -l -c "rvm install ruby-1.9.3-p547"  
RUN /bin/bash -l -c "rvm install ruby-2.1.5"  
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  
# make sure rvm is available in our shell when we run the container  
ONBUILD ENV USER appuser  
ONBUILD RUN /bin/bash -l -c "source /home/$USER/.rvm/scripts/rvm"  

