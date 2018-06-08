FROM phusion/baseimage:0.9.17  
  
MAINTAINER moltar <moltar@moltar.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PLENV_ROOT /usr/local/plenv  
ENV PATH $PLENV_ROOT/bin:$PATH  
ENV PLENV_INSTALL $PLENV_ROOT/bin/plenv_install_perl.sh  
  
ADD plenv_install_perl.sh $PLENV_INSTALL  
  
RUN apt-get update -qq && \  
apt-get install -y gcc make perl-modules patch && \  
mkdir -p $PLENV_ROOT/plugins/perl-build && \  
curl -L --silent https://github.com/tokuhirom/plenv/archive/2.1.1.tar.gz | tar
-xz --strip 1 -C $PLENV_ROOT && \  
curl -L --silent https://github.com/tokuhirom/Perl-Build/archive/1.12.tar.gz |
tar -xz --strip 1 -C $PLENV_ROOT/plugins/perl-build && \  
echo 'eval "$(plenv init -)"' >> /etc/profile.d/plenv.sh && \  
chmod 755 /etc/profile.d/plenv.sh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/sbin/my_init", "--", "plenv"]

