FROM cloudpg/centos-7-grid-tini  
LABEL maintainer="mirco.tracolli@pg.infn.it"  
LABEL Version=1.0  
  
# Dockerizing HTCondor nodes  
EXPOSE 5000  
EXPOSE 22  
# Environment variables  
ENV AMS_ADMIN="amsadmin"  
ENV AMS_ADMIN_HOME="/home/amsadmin/"  
# Default workingdir  
WORKDIR /root  
  
# Install packages  
RUN yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install binutils \  
boost-devel \  
cmake3 \  
curl \  
cvs \  
emacs \  
freetype \  
freetype-devel \  
fuse \  
gcc \  
gcc-c++ \  
git \  
glibc-devel \  
glibc-headers \  
gsl-devel \  
initscripts \  
krb5-workstation \  
libSM \  
libX11-devel \  
libXext \  
libXext-devel \  
libXft-devel \  
libXpm \  
libXpm-devel \  
make \  
man \  
nano \  
ncurses \  
ncurses-devel \  
openssh-clients \  
openssh-server \  
openssl098e \  
pam-krb5 \  
sudo \  
vim \  
&& yum clean all \  
# PREPARE AMS USER  
&& adduser $AMS_ADMIN -d $AMS_ADMIN_HOME \  
&& echo "$AMS_ADMIN:amspasswd" | chpasswd \  
&& echo "$AMS_ADMIN ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$AMS_ADMIN \  
&& chmod 0440 "/etc/sudoers.d/$AMS_ADMIN" \  
&& chown -R $AMS_ADMIN $AMS_ADMIN_HOME  
  
# Copy useful files  
COPY admin_home/setup_amsenv.sh admin_home/.bashrc $AMS_ADMIN_HOME  
  
# User setup  
RUN mkdir $AMS_ADMIN_HOME/.ssh \  
&& chown -R $AMS_ADMIN:$AMS_ADMIN $AMS_ADMIN_HOME/ \  
&& chmod u+x $AMS_ADMIN_HOME/setup_amsenv.sh  
  
# CONDOR and DODAS  
WORKDIR /etc/yum.repos.d  
  
RUN useradd -ms /bin/bash condor \  
&& wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-
rhel7.repo \  
&& wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-
rhel7.repo \  
&& wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor \  
&& rpm --import RPM-GPG-KEY-HTCondor \  
&& yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install condor-all python-pip \  
&& yum clean all \  
&& ln -s /usr/lib64/condor /usr/lib/condor \  
&& ln -s /usr/libexec/condor /usr/lib/condor/libexec \  
&& mkdir -p /var/log/dodas  
  
# HEALTHCHECKS  
RUN mkdir -p /opt/health/master/ /opt/health/executor/ /opt/health/submitter/
\  
&& pip install -U pip \  
&& pip install -U setuptools \  
&& pip install Flask supervisor supervisor-stdout  
  
# Copy useful files  
COPY etc/krb5.conf /etc/  
COPY etc/supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/  
COPY etc/condor/condor_config /etc/condor/  
COPY opt/healtcheck/executor/service.py /opt/healtcheck/executor/  
COPY opt/healtcheck/master/service.py /opt/healtcheck/master/  
COPY opt/healtcheck/submitter/service.py /opt/healtcheck/submitter/  
COPY etc/ssh/sshd_config /etc/ssh/  
COPY usr/local/sbin/run.sh /usr/local/sbin/  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Default workingdir  
WORKDIR /root  
  
# ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/sbin/run.sh"]  
# TEST ENTRYPOINT  
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/sbin/sshd", "-D"]  

