FROM reszelaz/leap-systemd  
  
RUN zypper ar -f
http://download.opensuse.org/repositories/home:/cmft/openSUSE_Leap_42.1 cmft  
RUN zypper --no-gpg-checks refresh cmft  
  
# install:  
# the echo command is a workaround for forcing the hostname during
installation  
# of tango-common. see: http://stackoverflow.com/a/28922278  
# vim - for easy editing of text files  
# xorg-x11-fonts - apparently necessary to run jive  
# glibc-locale is necessary for the en_US locale setting (tangosys user needs
it)  
RUN zypper install -y tango-db tango-test tango-java python-sardana vim \  
xorg-x11-fonts glibc-locale  
  
ENV TERM=xterm  
  
# add USER ENV (necessary e.g. for spyderlib)  
ENV USER=root  
  
# overwrite tangorc (/etc/tangorc is created with wrong TANGOHOST during
build)  
# a better solution may be http://stackoverflow.com/a/28922278 (but it didn't
work)  
COPY tangorc /etc/tangorc  
  
EXPOSE 10000  

