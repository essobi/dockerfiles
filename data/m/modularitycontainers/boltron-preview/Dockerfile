FROM baseruntime/baseruntime  
  
MAINTAINER "James Antill <james.antill@redhat.com>"  
ENV LANG=en_US.utf8 LC_ALL=en_US.UTF-8  
# ADD server.repo /etc/yum.repos.d  
RUN echo "modules=1" >> /etc/yum.repos.d/fedora-modular.repo  
  
ADD _copr_rpmsoftwaremanagement-dnf-nightly.repo /etc/yum.repos.d  
  
RUN microdnf install -y dnf glibc-langpack-en && microdnf clean all  
  
RUN dnf install -y
https://kojipkgs.fedoraproject.org//packages/modulemd/1.2.0/1.fc26/noarch/python3-modulemd-1.2.0-1.fc26.noarch.rpm
https://kojipkgs.fedoraproject.org//packages/PyYAML/3.12/3.fc26/x86_64/python3-PyYAML-3.12-3.fc26.x86_64.rpm
https://kojipkgs.fedoraproject.org//packages/libyaml/0.1.7/2.fc26/x86_64/libyaml-0.1.7-2.fc26.x86_64.rpm
&& dnf clean all  
  
RUN echo "" >> /etc/yum.repos.d/_copr_rpmsoftwaremanagement-dnf-nightly.repo  
RUN echo "exclude = dnf dnf-automatic dnf-conf dnf-yum python3-dnf" >>
/etc/yum.repos.d/_copr_rpmsoftwaremanagement-dnf-nightly.repo  
RUN echo "enabled=0" >> /etc/yum.repos.d/_copr_rpmsoftwaremanagement-dnf-
nightly.repo  
ADD _copr_mhatina-dnf.repo /etc/yum.repos.d  
  
# Added dep for python3-dnf: 2017-06-27  
RUN dnf install -y https://kojipkgs.fedoraproject.org//packages/python-
smartcols/0.2.0/3.fc26/x86_64/python3-smartcols-0.2.0-3.fc26.x86_64.rpm && dnf
clean all  
  
RUN dnf distro-sync -y dnf python3-dnf dnf-conf && dnf clean all  
RUN dnf distro-sync -y && dnf clean all  
  
ADD fedora-modular-rawhide.repo /etc/yum.repos.d  
ADD fedora-modular-nodejs.repo /etc/yum.repos.d  
  
ADD fedora-compat.repo /etc/yum.repos.d  
ADD fedora-compat-rawhide.repo /etc/yum.repos.d  
ADD fedora-compat-nodejs.repo /etc/yum.repos.d  
  
# To easily switch to compat. repos.  
ADD switch-to-compat.sh /  
  
# Get rid of this from the pure container?  
ADD modmd.patch /  
RUN microdnf install -y patch && microdnf clean all  
RUN patch -p0 < modmd.patch  
  
# nice prompt  
RUN cp -a /etc/skel/.bashrc /root/.bashrc  
  
# For debugging... (disabled by default)  
ADD rawhide.repo /etc/yum.repos.d  
  
#hacking in older version of nodejs to demonstrate updates  
RUN dnf -y module enable nodejs-f26 && \  
sed -i 's/version =/version =20170212165050/g'
/etc/dnf/modules.d/nodejs.module && \  
sed -i 's/profiles =/profiles =default/g' /etc/dnf/modules.d/nodejs.module &&
\  
dnf -y install --rpm https://ttomecek.fedorapeople.org/modular-
nodejs-6-10-2/nodejs-6.10.2-3.module_52f77d55.x86_64.rpm && \  
dnf -y install --rpm https://ttomecek.fedorapeople.org/modular-
nodejs-6-10-2/npm-3.10.10-1.6.10.2.3.module_52f77d55.x86_64.rpm  
  
CMD ['/bin/bash']  
  
LABEL RUN "/usr/bin/docker run -e container=docker -d" \  
'-v $PWD/machine-id:/etc/machine-id:Z' \  
'--stop-signal="SIGRTMIN+3"' \  
"--tmpfs /tmp --tmpfs /run" \  
"--security-opt=seccomp:unconfined" \  
"-v /sys/fs/cgroup/systemd:/sys/fs/cgroup/systemd" \  
"--name NAME" \  
"IMAGE /sbin/init"  
  

