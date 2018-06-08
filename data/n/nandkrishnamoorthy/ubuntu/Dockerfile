FROM ubuntu:16.04  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common python-software-properties  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:jonathonf/python-3.6  
RUN apt-get update  
RUN apt-get install -y sudo  
  
# Default sh to bash  
RUN echo "dash dash/sh boolean false" | debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
# Install the following utilities (required by poky)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential chrpath
curl diffstat gcc-multilib gawk git-core libsdl1.2-dev texinfo unzip wget
xterm  
  
# Additional host packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-client coreutils
libreadline-dev rpcbind nfs-common vim jq python python-setuptools python-yaml
device-tree-compiler  
  
# Additional host packages required by poky/scripts/wic  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y bzip2 dosfstools mtools
parted syslinux tree gettext parallel bsdmainutils wget ca-certificates apt-
transport-https  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y regina-rexx lib32z1
lib32stdc++6 autoconf bc flex bison libtool cpio libfdt-dev  
  
# install python 3 used by yocto packages to build  
RUN apt-get install -y python3.6 python3.6-dev python3-pip python3.6-venv  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk  
  
# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe  
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)"
/docker-java-home  
ENV JAVA_HOME /docker-java-home  
  
# update pip packages  
RUN python3.6 -m pip install pip --upgrade  
RUN python3.6 -m pip install wheel selenium  
  
# Add "repo" tool (used by many Yocto-based projects)  
RUN curl http://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo  
RUN chmod a+x /usr/local/bin/repo  
  
# Install Jfrog cli utility to deploy artifacts  
RUN cd /usr/bin; curl -fL https://getcli.jfrog.io | sh  
RUN chmod 755 /usr/bin/jfrog  
  
# Create a non-root user that will perform the actual build  
RUN id build 2>/dev/null || useradd --uid 1000 --create-home build  
RUN echo "build ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers  
  
# Fix error "Please use a locale setting which supports utf-8."  
# See https://wiki.yoctoproject.org/wiki/TipsAndTricks/ResolvingLocaleIssues  
RUN apt -y install locales && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
  
# install chrome  
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# install chromdriver  
RUN wget -N http://chromedriver.storage.googleapis.com/$(curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
-P ~/ \  
&& unzip ~/chromedriver_linux64.zip -d ~/ \  
&& rm ~/chromedriver_linux64.zip \  
&& sudo mv -f ~/chromedriver /usr/local/bin/chromedriver \  
&& sudo chown root:root /usr/local/bin/chromedriver \  
&& sudo chmod 0755 /usr/local/bin/chromedriver  
  
# Disable Host Key verification.  
RUN mkdir -p /home/build/.ssh  
RUN echo -e "Host *\n\tStrictHostKeyChecking no\n" > /home/build/.ssh/config  
RUN chown -R build:build /home/build/.ssh  
  
# delete all the apt list files since they're big and get stale quickly  
RUN rm -rf /var/lib/apt/lists/*  
  
# overwrite this with 'CMD []' in a dependent Dockerfile  
USER build  
ENV USER build  
WORKDIR /home/build  
CMD ["/bin/bash"]  

