FROM alisw/slc6-builder:latest  
  
RUN curl -L http://cvmrepo.web.cern.ch/cvmrepo/yum/RPM-GPG-KEY-CernVM >
/etc/pki/rpm-gpg/RPM-GPG-KEY-CernVM && \  
curl -L http://cvmrepo.web.cern.ch/cvmrepo/yum/cernvm.repo >
/etc/yum.repos.d/cernvm.repo && \  
rpm --rebuilddb && yum install -y cvmfs  
  
ENV CONDOR_SECRET="@mycondorpassword@" \  
PARROT_ALLOW_SWITCHING_CVMFS_REPOSITORIES=yes \  
PARROT_CVMFS_REPO=<default-repositories>\ alice-ocdb.cern.ch:url=http://cvmfs-
stratum-one.cern.ch/cvmfs/alice-
ocdb.cern.ch,pubkey=/etc/cvmfs/keys/cern.ch/cern-it1.cern.ch.pub \  
HTTP_PROXY=DIRECT; \  
PARROT_CVMFS_ALIEN_CACHE=/cvmfs_alien_cache  
  
RUN curl -o /etc/yum.repos.d/htcondor-development-rhel6.repo \  
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-
rhel6.repo && \  
rpm --rebuilddb && yum install -y condor  
  
COPY files/os-release /etc/os-release  
COPY files/cern-it1.cern.ch.pub /etc/cvmfs/keys/cern.ch/cern-it1.cern.ch.pub  
COPY files/cvmfs-default.local /etc/cvmfs/default.local  
COPY files/condor-container-pilot /tmp/condor-container-pilot  
  
RUN mkdir -p /cvmfs/alice-ocdb.cern.ch && mkdir -p /cvmfs/alice.cern.ch  
RUN chmod +x /tmp/condor-container-pilot  

