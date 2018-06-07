# Dockerfile to build a PBSpro-enabled container with extra packages needed to  
# run and test eHive  
# Cloned and updated version of the official pbspro image  
FROM pbspro/pbspro  
  
# Install essential things  
RUN yum install -y epel-release sudo git  
  
# Update the PBS config and create a pbsuser with a home directory and sudo
capability  
RUN sed -i 's/^adduser.*/export HOME=~pbsuser/' /entrypoint.sh \  
&& sed -i 's/PBS_START_MOM=0/PBS_START_MOM=1/' /etc/pbs.conf \  
&& useradd -r -m -U -G wheel -d /home/pbsuser -s /bin/bash -c "PBSpro user"
pbsuser \  
&& echo "pbsuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Clone the repos  
RUN mkdir /repo \  
&& git clone -b master https://github.com/Ensembl/ensembl-hive.git
/repo/ensembl-hive \  
&& git clone -b master https://github.com/Ensembl/ensembl-hive-pbspro.git
/repo/ensembl-hive-pbspro  
  
# Install all the dependencies  
RUN /repo/ensembl-hive/docker/setup_os.CentOS-7.sh \  
&& /repo/ensembl-hive/docker/setup_cpan.CentOS-7.sh /repo/ensembl-hive
/repo/ensembl-hive-pbspro  
  
ENV EHIVE_ROOT_DIR "/repo/ensembl-hive"  
ENV PATH "/repo/ensembl-hive/scripts:$PATH"  
ENV PERL5LIB "/repo/ensembl-hive/modules:/repo/ensembl-hive-
pbspro/modules:$PERL5LIB"  
ENV EHIVE_TEST_PIPELINE_URLS "sqlite:////home/pbsuser/"  
ENV EHIVE_MEADOW_TO_TEST "PBSPro"  
# Since the environment is set for the root user, but root is not allowed  
# to submit jobs, we need to login as pbsuser and preserve the environment  
CMD ["/bin/login", "-p", "-f", "pbsuser"]  
  

