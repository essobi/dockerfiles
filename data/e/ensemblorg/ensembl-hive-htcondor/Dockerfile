# Dockerfile to build a Condor-enabled container with extra packages needed to  
# run and test eHive  
# Cloned and updated version of our docker-htcondor container  
FROM ensemblorg/docker-htcondor  
  
# Install git  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update -y && apt-get install -y git && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Clone the repos  
RUN mkdir /repo \  
&& git clone -b master https://github.com/Ensembl/ensembl-hive.git
/repo/ensembl-hive \  
&& git clone -b master https://github.com/Ensembl/ensembl-hive-htcondor.git
/repo/ensembl-hive-htcondor  
  
# Install all the dependencies  
RUN /repo/ensembl-hive/docker/setup_os.Ubuntu-14.04.sh \  
&& /repo/ensembl-hive/docker/setup_cpan.Ubuntu-14.04.sh /repo/ensembl-hive
/repo/ensembl-hive-htcondor  
  
ENV EHIVE_ROOT_DIR "/repo/ensembl-hive/"  
ENV PATH "/repo/ensembl-hive/scripts:$PATH"  
ENV PERL5LIB "/repo/ensembl-hive/modules:/repo/ensembl-hive-
htcondor/modules:$PERL5LIB"  
ENV EHIVE_TEST_PIPELINE_URLS "sqlite:////home/condoradmin/"  
ENV EHIVE_MEADOW_TO_TEST "HTCondor"  
# Since the environment is set for the root user, but root is not allowed  
# to submit jobs, we need to login as condoradmin and preserve the environment  
CMD ["/bin/login", "-p", "-f", "condoradmin"]  

