FROM fedora:latest  
MAINTAINER [Martin Babinsky martbab@gmail.com]  
  
RUN echo 'deltarpm = false' >> /etc/dnf/dnf.conf \  
&& dnf update -y dnf \  
&& dnf install -y dnf-plugins-core sudo dnf-plugins-extras wget \  
&& dnf config-manager --set-enabled updates-testing \  
&& dnf copr enable -y @freeipa/freeipa-4-4 \  
# FIXME: due to packaging issues the following is not a dependency of  
# python{2,3}-rpm-macros, and must be installed manually  
&& dnf install -y python-srpm-macros \  
&& dnf clean all  
  
# install build dependencies from COPR and latest devel branch  
RUN dnf install -y @buildsys-build @development-tools \  
&& dnf repository-packages group_freeipa-freeipa-4-4 install -y \  
&& wget
https://raw.githubusercontent.com/freeipa/freeipa/ipa-4-4/freeipa.spec.in \  
&& dnf builddep -y \--spec ./freeipa.spec.in --best --allowerasing \  
&& dnf clean all \  
&& rm -f ./freeipa.spec.in  
  
# update everything and try to resolve conflicts  
RUN dnf update -y \--best --allowerasing && dnf clean all  

