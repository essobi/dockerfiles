# This Dockerfile is more complicated than one would expect it to be. This is  
# for good reason, though.  
#  
# Initially it simply installed the Zuul package from PyPI. But this doesn't  
# work, because the package on PyPI is broken: it doesn't contain the static
web  
# (HTML, JS,...) files.  
#  
# These ought to be build during `python setup.py sdist`-time, but: this only  
# happens when `yarn` is installed on the system. If not, `sdist` happily  
# continues and builds a, basically, broken package.  
#  
# Anyway, this should work.  
# Step one: build sdist package  
FROM docker.io/alpine:3.7 as builder  
  
ARG version=3.0.3  
RUN apk add --no-cache git python py-setuptools yarn  
USER nobody  
RUN cd /tmp && \  
git clone -b $version https://github.com/openstack-infra/zuul.git && \  
cd zuul && \  
python setup.py sdist  
  
# Step two: build bubblewrap  
FROM docker.io/centos:7.4.1708 as builder2  
  
ARG bubblewrap_version=0.2.1  
RUN yum install -y \  
gcc \  
libcap-devel \  
make \  
&& \  
cd /tmp && \  
curl -LO
https://github.com/projectatomic/bubblewrap/releases/download/v$bubblewrap_version/bubblewrap-$bubblewrap_version.tar.xz
&& \  
tar xvf bubblewrap-$bubblewrap_version.tar.xz && \  
cd bubblewrap-$bubblewrap_version && \  
./configure --prefix=/usr/local && \  
make && \  
yum remove -y \  
gcc \  
libcap-devel \  
make \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum  
  
# Step three: use sdist package and bubblewrap and build the 'runtime'  
# container  
FROM docker.io/centos:7.4.1708  
# Install runtime dependencies  
RUN yum install -y \  
https://centos7.iuscommunity.org/ius-release.rpm && \  
yum install -y \  
git \  
libffi \  
python35u \  
re2 \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum  
  
VOLUME /etc/zuul  
  
RUN adduser --system zuul --home-dir /var/lib/zuul --create-home  
VOLUME /var/lib/zuul/.ssh  
  
COPY \--from=builder2 /tmp/bubblewrap-*/bwrap /usr/local/bin/bwrap  
# Note: bwrap needs setuid on 'old' kernels  
RUN chown root:root /usr/local/bin/bwrap && chmod 4755 /usr/local/bin/bwrap  
  
COPY \--from=builder /tmp/zuul/dist/zuul-*.tar.gz .  
  
# Install build-time dependencies, package and remove build-time dependencies  
# Note: not removing libffi-devel due to  
# https://bugs.centos.org/view.php?id=10828  
RUN yum install -y \  
gcc \  
gcc-c++ \  
libffi-devel \  
python35u-devel \  
python35u-pip \  
re2-devel \  
which \  
&& \  
pip3.5 install zuul-*.tar.gz && \  
rm -rf ~/.cache/pip zuul-*.tar.gz && \  
yum remove -y \  
gcc \  
gcc-c++ \  
python35u-devel \  
python35u-pip \  
re2-devel \  
which \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum  
  
COPY zuul-gearman.py /zuul-gearman.py  
  
USER zuul:zuul  
ENTRYPOINT ["zuul", "-c", "/etc/zuul/zuul.conf"]  

