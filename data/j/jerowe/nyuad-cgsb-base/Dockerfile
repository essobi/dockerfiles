FROM centos:centos6  
  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
RUN yum install -y tree git openssh-server openssh-clients which python-pip  
RUN yum install -y environment-modules curl  
RUN yum install -y wget curl glibc-devel  
RUN yum update -y && yum upgrade -y && yum -y clean all  
  
RUN mkdir -p /var/run/sshd && \  
echo "root:root" | chpasswd  
  
#Make some users  
RUN adduser "testuser" -m && \  
echo "testuser:testuser" | chpasswd  
USER testuser  
RUN mkdir /home/testuser/.ssh  
ADD id_rsa.pub /home/testuser/.ssh/authorized_keys  
  
USER root  
RUN adduser "easybuild" -m && \  
echo "easybuild:easybuild" | chpasswd  
#RUN mkdir /home/easybuild  
# Start SSH service  
USER root  
  
RUN service sshd start  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
RUN /bin/date  
  
# Now lets install Easybuild!  
USER root  
RUN mkdir -p /opt/easybuild  
RUN chown easybuild:easybuild /opt/easybuild  
  
USER easybuild  
ENV EASYBUILD_PREFIX=/opt/easybuild  
WORKDIR /opt/easybuild  
RUN which modulecmd  
#RUN curl -O https://raw.githubusercontent.com/hpcugent/easybuild-
framework/develop/easybuild/scripts/bootstrap_eb.py  
#RUN python2 bootstrap_eb.py $EASYBUILD_PREFIX  
#RUN module use $EASYBUILD_PREFIX/modules/all  
#RUN module load EasyBuild  
# Install miniconda  
USER root  
RUN mkdir -p /tmp/conda-build && wget
http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/anaconda3  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PATH=/opt/anaconda3/bin:$PATH  
RUN rm Miniconda3-latest-Linux-x86_64.sh  
  
# Subscripe to channels  
RUN conda config --add channels bioconda  
RUN conda config --add channels r  
  
# Do some base installs  
RUN conda install -y gcc perl-app-cpanminus perl-termreadkey r r-base
r-essentials java-jdk  
RUN conda install -y perl-net-ssleay  
RUN cpanm --quiet Task::Moose MooseX::Getopt::Usage::Role::Man  
RUN cpanm --quiet HPC::Runner HPC::Runner::Scheduler  
RUN cpanm --quiet HPC::Runner::Slurm HPC::Runner::PBS  
RUN cpanm --quiet HPC::Runner::MCE  
RUN cpanm --quiet BioX::Workflow  
RUN git config --global user.name 'My Name'  
RUN git config --global user.email 'email@google.com'  
RUN cpanm --verbose Git::Wrapper  
RUN cpanm --notest --quiet --skip-satisfied Dist::Milla  
  
EXPOSE 10389 22  

