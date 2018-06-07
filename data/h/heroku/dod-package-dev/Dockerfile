FROM ubuntu:trusty  
  
# let's make apt list package versions, since those are handy during devel  
RUN echo 'APT::Get::Show-Versions "1";' > /etc/apt/apt.conf.d/verbose  
  
# normal build deps  
RUN apt-get update && apt-get install -y \  
autopkgtest \  
bash-completion curl less rsync vim wget \  
build-essential \  
debian-keyring \  
devscripts \  
dh-make dh-golang\  
dput-ng \  
equivs autotools-dev\  
git bzr mercurial subversion \  
git-buildpackage svn-buildpackage \  
libcrypt-ssleay-perl \  
libdistro-info-perl \  
libfile-fcntllock-perl \  
libwww-perl \  
lintian \  
openssh-client \  
pristine-tar \  
python-distro-info \  
python3-debian \  
quilt \  
reprepro \  
sudo \  
ubuntu-dev-tools pbuilder \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# need deb-src for compiling packages  
RUN find /etc/apt/sources.list* -type f -exec sed -i 'p; s/^deb /deb-src /'
'{}' +  
  
RUN echo 'ALL ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/allusers-nopass  
  
ENV HOME /root  
RUN { \  
echo "export DEBFULLNAME='' DEBEMAIL=''"; \  
echo 'dch -i -D precise'; \  
echo 'uscan --force-download --verbose --download-current-version'; \  
echo 'debuild -S -uc'; \  
echo 'cd /usr/src/postgresql'; \  
} >> ~/.bash_history  
  
ENV LANG C.UTF-8  
ENV TERM xterm-256color  
RUN cp /etc/skel/.bashrc ~/ \  
&& sed -ri 's/^#(force_color_prompt=yes)/\1/' ~/.bashrc  
  
ENV QUILT_PATCHES debian/patches  
ENV QUILT_REFRESH_ARGS -p ab --no-timestamps --no-index  
  
# make sure pbuilder-dist uses a sane default mirror  
ENV UBUNTUTOOLS_DEBIAN_MIRROR http://httpredir.debian.org/debian  
  
RUN { \  
echo "APTCACHEHARDLINK='no'"; \  
} >> ~/.pbuilderrc  
  
COPY scripts /heroku  
RUN /heroku/apt.postgresql.org.sh  

