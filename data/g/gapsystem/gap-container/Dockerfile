FROM ubuntu:bionic  
  
MAINTAINER The GAP Group <support@gap-system.org>  
  
RUN dpkg \--add-architecture i386 \  
&& apt-get update -qq \  
&& apt-get -qq install -y autoconf build-essential m4 libreadline6-dev
libncurses5-dev wget \  
unzip libgmp3-dev cmake gcc-multilib gcc g++ sudo  
  
RUN adduser \--quiet \--shell /bin/bash \--gecos "GAP user,101,," \--disabled-
password gap \  
&& adduser gap sudo \  
&& chown -R gap:gap /home/gap/ \  
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \  
&& cd /home/gap \  
&& touch .sudo_as_admin_successful  
  
RUN mkdir -p /home/gap/inst \  
&& cd /home/gap/inst \  
&& wget https://www.gap-system.org/pub/gap/gap4core/gap-4.9.1-core.zip \  
&& unzip gap-4.9.1-core.zip \  
&& rm gap-4.9.1-core.zip \  
&& cd gap-4.9.1 \  
&& wget https://www.gap-system.org/Manuals/gap-4.9.1-manuals.tar.gz \  
&& tar xvzf gap-4.9.1-manuals.tar.gz \  
&& rm gap-4.9.1-manuals.tar.gz \  
&& ./autogen.sh \  
&& ./configure \--with-gmp=system \  
&& make \  
&& cp bin/gap.sh bin/gap \  
&& mkdir pkg \  
&& cd pkg \  
&& wget https://www.gap-system.org/pub/gap/gap4pkgs/packages-required-
stable-v4.9.1.tar.gz \  
&& tar xvzf packages-required-stable-v4.9.1.tar.gz \  
&& rm packages-required-stable-v4.9.1.tar.gz \  
&& chown -R gap:gap /home/gap/inst  
# Set up new user and home directory in environment.  
# Note that WORKDIR will not expand environment variables in docker versions <
1.3.1.  
# See docker issue 2637: https://github.com/docker/docker/issues/2637  
USER gap  
ENV HOME /home/gap  
ENV GAP_HOME /home/gap/inst/gap-4.9.1  
ENV PATH ${GAP_HOME}/bin:${PATH}  
  
# Start at $HOME.  
WORKDIR /home/gap  
# Start from a BASH shell.  
CMD ["bash"]  

