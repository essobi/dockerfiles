FROM cloudpg/centos-7-grid:singularity  
LABEL maintainer="mirco.tracolli@pg.infn.it"  
LABEL Version=1.0  
  
# HTCondor  
# https://get.onedata.org/oneclient.sh  
WORKDIR /etc/yum.repos.d  
  
RUN useradd -ms /bin/bash condor \  
&& wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-
rhel7.repo \  
&& wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-
rhel7.repo \  
&& wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor \  
&& rpm --import RPM-GPG-KEY-HTCondor \  
&& wget -O onedata.repo http://packages.onedata.org/yum/onedata_centos_7x.repo
\  
&& yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install condor-all-8.6.5 \  
&& yum clean all \  
&& ln -s /usr/lib64/condor /usr/lib/condor \  
&& ln -s /usr/libexec/condor /usr/lib/condor/libexec  
  
COPY condorconfig/* /etc/condor/  
COPY config.d/* /etc/condor/config.d/  
COPY dodas_bin/* /usr/local/bin/  
RUN mkdir -p /etc/condor/certs \  
&& mkdir -p /etc/cvmfs/SITECONF \  
&& cp /etc/condor/config.d/condor_mapfile /etc/condor/certs/condor_mapfile \  
&& rm /etc/condor/config.d/condor_mapfile  
  
WORKDIR /root  
  
# Download validation script  
RUN wget
https://gitlab.cern.ch/CMSSI/CMSglideinWMSValidation/raw/master/singularity_validation.sh
\  
&& wget
https://gitlab.cern.ch/CMSSI/CMSglideinWMSValidation/raw/master/singularity_wrapper.sh
-O /usr/local/libexec/singularity_wrapper.sh  
  
RUN chmod +x /usr/local/bin/dodasexe_pre.sh \  
&& chmod +x /usr/local/bin/dodasexe.sh \  
&& chmod +x /usr/local/bin/dodas.sh \  
&& chmod +x /usr/local/libexec/singularity_wrapper.sh \  
&& chmod 0755 /usr/local/libexec/singularity_wrapper.sh \  
&& chown condor:condor /usr/local/libexec/singularity_wrapper.sh \  
# onedata directories needed by mount  
&& mkdir -p /mnt/onedata/ /var/log/dodas  

