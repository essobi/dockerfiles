FROM centos:7  
ENV OPENSHIFT_VERSION "v3.9.0"  
ENV OPENSHIFT_TAG "191fece"  
ARG RUNTIME_DEPS="git gettext"  
RUN yum -q -y update && \  
rpm --quiet --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \  
yum -q -y install ${RUNTIME_DEPS} && \  
curl -OLs
https://github.com/openshift/origin/releases/download/${OPENSHIFT_VERSION}/openshift-
origin-client-tools-${OPENSHIFT_VERSION}-${OPENSHIFT_TAG}-linux-64bit.tar.gz
&& \  
curl -OLs
https://github.com/openshift/origin/releases/download/${OPENSHIFT_VERSION}/CHECKSUM
&& \  
grep "openshift-origin-client-
tools-${OPENSHIFT_VERSION}-${OPENSHIFT_TAG}-linux-64bit.tar.gz" CHECKSUM >
CHECK && \  
sha256sum -c CHECK && \  
tar -zxf openshift-origin-client-
tools-${OPENSHIFT_VERSION}-${OPENSHIFT_TAG}-linux-64bit.tar.gz && \  
mv openshift-origin-client-
tools-${OPENSHIFT_VERSION}-${OPENSHIFT_TAG}-linux-64bit/oc /usr/local/bin/ &&
\  
chmod +x /usr/local/bin/oc && \  
yum -q clean all && \  
rm -rf openshift-origin-client-
tools-${OPENSHIFT_VERSION}-${OPENSHIFT_TAG}-linux-64bit* CHECK* && \  
oc version  
  
ENTRYPOINT []  

