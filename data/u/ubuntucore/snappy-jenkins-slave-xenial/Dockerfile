FROM ubuntucore/jenkins-swarm-slave-ubuntu:xenial  
  
USER root  
  
# ubuntu-device-flash uses parts of snappy that try to reload udev rules when  
# processing oem snaps, which this is not needed at build time; udev is not  
# not available in the container, making a symlink solves the dependency
without  
# affecting the build process  
RUN ln -s /bin/true /usr/local/bin/udevadm  
  
# install ppas  
RUN apt-get update && apt-get install --no-install-recommends -qy \  
python-software-properties \  
software-properties-common && rm -rf /var/lib/apt/lists/*  
RUN add-apt-repository -y ppa:snappy-dev/tools-proposed  
  
# install dependencies  
RUN apt-get update && apt-get install --no-install-recommends -qy \  
build-essential \  
ca-certificates \  
dput \  
grub-common \  
lintian \  
python-junitxml \  
sudo subunit \  
snappy-cloud-image \  
snappy-tests-job \  
squashfs-tools \  
ubuntu-core-security-utils \  
openssh-client \  
# snapcraft dependencies  
bzr devscripts dpkg-dev equivs git mercurial pyflakes \  
python3-apt python3-docopt python3-coverage \  
python3-fixtures python3-jsonschema python3-lxml \  
python3-magic python3-mccabe python3-pep8 python3-petname \  
python3-pexpect python3-pip python3-progressbar python3-pymacaroons \  
python3-requests python3-requests-oauthlib python3-requests-toolbelt \  
python3-simplejson python3-ssoclient python3-testscenarios python3-testtools \  
python3-xdg python3-yaml \  
snapcraft && rm -rf /var/lib/apt/lists/*  
  
# update SSL certificates  
RUN update-ca-certificates -f  
  
# make jenkins-slave sudoer  
RUN echo "jenkins-slave ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# ssh config  
RUN mkdir -p /home/jenkins-slave/.ssh  
COPY config/ssh /home/jenkins-slave/.ssh/config  
RUN chown -R jenkins-slave:jenkins-slave /home/jenkins-slave/.ssh  

