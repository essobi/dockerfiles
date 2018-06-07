FROM ubuntu:18.04  
MAINTAINER Mike Baynton <mike@mbaynton.com>  
  
# install packages needed to do much of anything  
# iproute2 for /sbin/ip, used by xdebug2host.sh  
RUN apt-get update && apt-get install -y apt-utils curl git bzip2 iproute2 &&
apt-get clean  
  
# install a few libraries php pretty much always should have  
RUN apt-get install -y libxml2 libssl-dev libxslt1.1 libtidy5 libmcrypt4
libjpeg8 libicu60 libpng16-16 libcurl4 && apt-get clean  
  
# install phpenv  
ENV PHPENV_ROOT /usr/local/phpenv  
RUN /usr/bin/curl
https://raw.githubusercontent.com/CHH/phpenv/master/bin/phpenv-install.sh |
bash  
  
# Add phpenv and prophusion to the default PATH for noninteractive shells  
RUN echo 'PATH="/usr/local/phpenv/bin:$PATH"' >> /etc/environment  
  
# Setup $PATH for phpenv and the php binaries the system should be finding.  
RUN echo 'export PATH="/usr/local/phpenv/bin:$PATH"' >
/etc/bash.bashrc.phpenv_setup \  
&& echo 'eval "$(phpenv init -)"' >> /etc/bash.bashrc.phpenv_setup \  
&& echo '. /etc/bash.bashrc.phpenv_setup' >> /etc/bash.bashrc \  
&& echo '18.04' > /prophusion_build_target  
  
# Make the location of the php environments a volume  
VOLUME /usr/local/phpenv/versions  
  
# RUN ["/bin/bash", "-c", "source /etc/bash.bashrc.phpenv_setup"]  
# Make a place to unpack php builds before we have verified their hashes  
RUN mkdir /usr/local/phpenv/versions/.unverified  
RUN ["/bin/bash", "-c", "chmod a+rwx -R /usr/local/phpenv/versions"]  
  
# Install prophusion script  
COPY prophusion.sh /usr/local/phpenv/bin/prophusion  
# Install xdebug2host script  
COPY xdebug2host.sh /usr/local/bin/xdebug2host  
  
# Make a link in /usr/local/bin. This makes it easier to run `docker exec
[container] prophusion ...` from the host.  
RUN ln -s /usr/local/phpenv/bin/prophusion /usr/local/bin/prophusion  
  
COPY prophusion-base-entrypoint.sh /prophusion-base-entrypoint.sh  
ENTRYPOINT ["/prophusion-base-entrypoint.sh"]  

