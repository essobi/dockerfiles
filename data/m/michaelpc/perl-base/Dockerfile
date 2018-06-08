FROM perl:threaded  
  
ENV TERM xterm  
  
RUN mkdir /tmp/installation  
  
WORKDIR /tmp/installation  
  
RUN apt-get update; \  
apt-get install -y apt-utils \  
software-properties-common \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
wget gdebi-core \  
vim \  
screen \  
htop \  
exuberant-ctags \  
ntp \  
ntpdate;  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb -cO /tmp/installation/dumb-init.deb; \  
dpkg -i /tmp/installation/dumb-init.deb; \  
apt-get update; \  
apt-get upgrade -y; \  
apt-get autoremove -y;  
  
RUN HOME=/tmp/installation cpanm --notest Carton \  
Archive::Tar::Wrapper \  
Dist::Zilla \  
Dist::Zilla::Plugin::Prereqs::FromCPANfile \  
App::Munner \  
Term::ReadLine \  
Term::ReadLine::Perl \  
Term::ReadKey Capture::Tiny;  
  
ADD ./service.pl /usr/local/bin/service.pl  
  
RUN chmod +x /usr/local/bin/service.pl  
  
RUN rm -fr /tmp/installation  
  
WORKDIR /app  
  
VOLUME /app  
  
ENTRYPOINT [ "/usr/bin/dumb-init", "/usr/local/bin/service.pl" ]  

