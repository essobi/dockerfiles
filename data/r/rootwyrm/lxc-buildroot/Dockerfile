FROM vbatts/slackware:latest  
## The magic begins...  
MAINTAINER Phillip "RootWyrm" Jaenke <docker@rootwyrm.com>  
  
## We always use label.  
LABEL com.rootwyrm.vendor="RootWyrm"  
LABEL com.rootwyrm.version="0.0.1"  
LABEL com.rootwyrm.branch="master"  
LABEL com.rootwyrm.release=""  
LABEL com.rootwyrm.vcs-type="git"  
LABEL com.rootwyrm.changelog-url="/CHANGELOG"  
  
LABEL com.rootwyrm.rootcore.base="slackware:latest"  
LABEL com.rootwyrm.rootcore.depends=""  
LABEL com.rootwyrm.rootcore.provides="buildroot"  
LABEL com.rootwyrm.rootcore.svctype="compiler, builder"  
LABEL com.rootwyrm.rootcore.ports="22"  
LABEL com.rootwyrm.rootcore.qnap_compatible="false"  
LABEL com.rootwyrm.rootcore.synology_compatible="false"  
  
ENV BATCH=y DEFAULT_ANSWER=y  
  
RUN rm /etc/slackpkg/mirrors  
ADD mirrors /etc/slackpkg/mirrors  
RUN slackpkg update gpg && slackpkg update  
RUN slackpkg install wget  
WORKDIR /root  
## Retrieve slackpkg+  
RUN wget -r -nH --no-parent --reject "index.html*" \--reject "robots.txt"
\--cut-dirs=2 http://slakfinder.org/slackpkg+/pkg/  
RUN /sbin/installpkg --terse --md5sum slackpkg+*.t?z  
## Have to rerun update due to slackpkg+ extension  
RUN slackpkg update gpg && slackpkg update  
RUN slackpkg install -batch=on -default_answer=y \  
bc-* binutils-* bzip2-* cpio gcc-4* "gcc-g++* "git-* gzip-* ncurses-5* \  
make-* gccmakedep-* makedepend-* mercurial whois patch-* perl-5* \  
python-2.7* rsync sed-* infozip logrotate  
## Clean up because I don't like messes.  
RUN rm /root/slackpkg*  
## ssh install done separate if we need to remove  
RUN slackpkg install -batch=on -default_answer=y openssh-*  
  
WORKDIR /root  
## Pull master  
RUN git clone git://git.buildroot.net/buildroot -b 2015.11.x --depth=1  
WORKDIR /root/buildroot  
RUN touch .config  
RUN touch kernel.config  
  
## NOTE: Can't redirect slackpkg due to limitations in it. Somewhat annoying,
that.  
RUN echo "30 6 * * 0,2,4 root /usr/sbin/slackpkg -batch=on -default_answer=n
update" >> /etc/crontab  
RUN echo "# Comment to disable weekly repository updates." >> /etc/crontab  
RUN echo "0 9 * * 0 root cd /root/buildroot ; /bin/git pull" >> /etc/crontab  
#ADD /etc/logrotate.d/ /etc/logrotate.d/  
VOLUME /root/buildroot/dl  
VOLUME /buildroot_output  
  
## Enable ssh  
EXPOSE 22  
CMD ["/bin/bash"]  

