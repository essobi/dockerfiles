#
------------------------------------------------------------------------------  
# Based on a work at https://github.com/docker/docker.  
#
------------------------------------------------------------------------------  
# Pull base image.  
From ubuntu  
MAINTAINER Almagest fraternite <almagestfraternite@gmail.com>  
  
#
------------------------------------------------------------------------------  
# Install base  
RUN sed -i'' 's/archive\\.ubuntu\\.com/us\\.archive\\.ubuntu\\.com/'
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5  
  
RUN apt-get update  
RUN apt-get install nano libnet-ifconfig-wrapper-perl software-properties-
common python-software-properties wget sudo apt-utils graphicsmagick
libdigest-hmac-perl libfile-copy-recursive-perl libio-tee-perl libunicode-
string-perl libmail-imapclient-perl libterm-readkey-perl makepasswd rcs perl-
doc libio-tee-perl git libmail-imapclient-perl libdigest-md5-file-perl
libterm-readkey-perl libfile-copy-recursive-perl build-essential make automake
libunicode-string-perl makepasswd libauthen-ntlm-perl libcrypt-ssleay-perl
libdigest-hmac-perl libfile-copy-recursive-perl libio-compress-perl libio-
socket-inet6-perl libio-socket-ssl-perl libio-tee-perl libmodule-scandeps-perl
libnet-ssleay-perl libpar-packer-perl libreadonly-perl libterm-readkey-perl
libtest-pod-perl libtest-simple-perl libunicode-string-perl liburi-perl
cpanminus tmux -y --fix-missing  
  
RUN wget
https://gist.githubusercontent.com/lanmower/38e6175febd8b9a567cc9755ce7221db/raw/ad869f2abf0e56e0c83a3b7595e583de3d04f131/ffdshow.sh
-O /tmp/ffmpeg.sh  
RUN chmod +x /tmp/ffmpeg.sh  
RUN /tmp/ffmpeg.sh  
  
# Install Supervisor.  
RUN \  
apt-get update && \  
apt-get install -y supervisor && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf  
  
# Define mountable directories.  
VOLUME ["/etc/supervisor/conf.d"]  
  
#
------------------------------------------------------------------------------  
# Security changes  
# - Determine runlevel and services at startup [BOOT-5180]  
# - Check the output of apt-cache policy manually to determine why output is
empty [KRNL-5788]  
RUN apt-get update | apt-get upgrade -y  
  
# - Install a PAM module for password strength testing like pam_cracklib or
pam_passwdqc [AUTH-9262]  
RUN apt-get install libpam-cracklib -y  
RUN ln -s /lib/x86_64-linux-gnu/security/pam_cracklib.so /lib/security  
  
# Define working directory.  
WORKDIR /etc/supervisor/conf.d  
  
RUN apt-get install -y openssh-server locales  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
RUN useradd user  
RUN mkdir /home/user  
RUN chown user /home/user  
  
RUN echo 'root:almagest1298' | chpasswd  
RUN echo 'user:almagest1298' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN apt-get install -y --fix-missing build-essential g++ curl libssl-dev
apache2-utils git libxml2-dev sshfs cpanminus makepasswd rcs perl-doc libio-
tee-perl git libmail-imapclient-perl libdigest-md5-file-perl libterm-readkey-
perl libfile-copy-recursive-perl build-essential make automake libunicode-
string-perl libauthen-ntlm-perl libcrypt-ssleay-perl libdigest-hmac-perl
libfile-copy-recursive-perl libio-compress-perl libio-socket-inet6-perl libio-
socket-ssl-perl libio-tee-perl libmodule-scandeps-perl libnet-ssleay-perl
libpar-packer-perl libterm-readkey-perl libtest-pod-perl libtest-simple-perl
libunicode-string-perl liburi-perl cpanminus  
  
# Set the locale  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen &&
locale-gen  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN cpanm "Class::Load"  
RUN cpanm "Crypt::OpenSSL::RSA"  
RUN cpanm "Data::Uniqid"  
RUN cpanm "Dist::CheckConflicts"  
RUN cpanm "JSON"  
RUN cpanm "JSON::WebToken"  
RUN cpanm "JSON::WebToken::Crypt::RSA"  
RUN cpanm "Module::Implementation"  
RUN cpanm "Module::Runtime"  
RUN cpanm "Package::Stash"  
RUN cpanm "Package::Stash::XS"  
RUN cpanm "Readonly"  
RUN cpanm "Sys::MemInfo"  
RUN cpanm "Test::Fatal"  
RUN cpanm "Test::Mock::Guard"  
RUN cpanm "Test::MockObject"  
RUN cpanm "Test::Requires"  
RUN cpanm "Try::Tiny"  
  
WORKDIR /usr/src  
RUN export PERL_MM_USE_DEFAULT=1  
RUN perl -MCPAN -e 'install Unicode::String'  
RUN cd /usr/src  
RUN git clone git://github.com/imapsync/imapsync.git /usr/src/imapsync  
RUN cd /usr/src/imapsync  
RUN mkdir dist  
#RUN make install  
#
------------------------------------------------------------------------------  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
#RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
#
------------------------------------------------------------------------------  
# Install Cloud9  
RUN git clone https://github.com/c9/core.git /cloud9  
WORKDIR /cloud9  
RUN scripts/install-sdk.sh  
RUN chmod a+rw /cloud9  
  
# Tweak standlone.js conf  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
  
# Define mountable directories.  
VOLUME ["/etc/supervisor/conf.d"]  
  
#
------------------------------------------------------------------------------  
# Security changes  
# - Determine runlevel and services at startup [BOOT-5180]  
RUN update-rc.d supervisor defaults  
  
# Define working directory.  
WORKDIR /etc/supervisor/conf.d  
  
# Add supervisord conf  
ADD conf/cloud9.conf /etc/supervisor/conf.d/  
ADD conf/sshd.conf /etc/supervisor/conf.d/  
ADD conf/cron.conf /etc/supervisor/conf.d/  
  
#
------------------------------------------------------------------------------  
# Add volumes  
RUN mkdir /workspace  
RUN mkdir /store  
RUN mkdir /store/cfs  
  
RUN curl https://install.meteor.com/ | sh  
  
#
------------------------------------------------------------------------------  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#
------------------------------------------------------------------------------  
# Expose ports.  
EXPOSE 22  
EXPOSE 80  
EXPOSE 3000  
EXPOSE 4000  
EXPOSE 5000  
#
------------------------------------------------------------------------------  
# Start supervisor, define default command.  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-u", "root"]  

