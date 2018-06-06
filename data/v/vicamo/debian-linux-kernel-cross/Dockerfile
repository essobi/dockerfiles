# GENERATED from Dockerfile.template. DO NOT EDIT.  
FROM vicamo/debian-linux-kernel:stretch-amd64  
  
RUN apt-get update -qq \  
&& (if test -n "$(apt-cache search crossbuild-essential- | grep '^crossbuild-
essential-mips ')"; then \  
apt-get install --no-install-recommends -y crossbuild-essential-mips; \  
else \  
apt-get build-dep -y build-essential \  
&& mkdir -p /tmp/build-essential \  
&& (cd /tmp/build-essential \  
&& apt-get source build-essential) \  
&& (cd $(ls -d /tmp/build-essential/build-essential-*) \  
&& sed -i 's/^#//' debian/cross-targets \  
&& debian/rules debian/control \  
&& fakeroot debian/rules binary) \  
&& (dpkg -i /tmp/build-essential/crossbuild-essential-mips_*.deb \  
|| apt install --no-install-recommends --fix-broken -y) \  
&& rm -rf /tmp/build-essential; \  
fi)  

