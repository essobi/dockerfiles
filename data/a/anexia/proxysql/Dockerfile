FROM debian:stretch-slim  
  
MAINTAINER Stephan Peijnik <speijnik@anexia-it.com>  
  
ARG dumb_init_version=1.2.0  
ARG dumb_init_base_url=https://github.com/Yelp/dumb-
init/releases/download/v${dumb_init_version}  
ARG dumb_init_package_name=dumb-init_${dumb_init_version}_amd64.deb  
  
ARG proxysql_version=1.4.3  
ARG
proxysql_base_url=https://github.com/sysown/proxysql/releases/download/v${proxysql_version}  
ARG proxysql_package_name=proxysql_${proxysql_version}-debian9_amd64.deb  
ARG proxysql_package_md5sum=3ac106603cf007b4255f90999597ebfb  
  
# In a single step (and thus layer), do the following:  
# * Install wget, ca-certificates and libssl1.1  
# * Fetch the dumb-init Debian package, verify its sha256sum and install it  
# * Fetch the proxysql Debian package, verify its md5sum and install it  
# * Remove wget and ca-certificates again  
# * Run apt-get autoremove to remove everything no package depends on  
# * Clear /var/lib/apt/lists and run apt-get clean  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
wget ca-certificates libssl1.1 && \  
wget ${dumb_init_base_url}/${dumb_init_package_name} \  
-O /tmp/${dumb_init_package_name} && \  
wget ${dumb_init_base_url}/sha256sums -O /tmp/sha256sums && \  
cd /tmp && \  
sha256sum -c --ignore-missing sha256sums && \  
rm /tmp/sha256sums && \  
dpkg -i /tmp/${dumb_init_package_name} && \  
rm -f /tmp/${dumb_init_package_name} && \  
wget ${proxysql_base_url}/${proxysql_package_name} \  
-O /tmp/${proxysql_package_name} && \  
echo "${proxysql_package_md5sum} */tmp/${proxysql_package_name}" \  
> /tmp/md5sums && \  
md5sum -c /tmp/md5sums && \  
rm /tmp/md5sums && \  
dpkg -i /tmp/${proxysql_package_name} && \  
rm -f /tmp/${proxysql_package_name} && \  
apt-get remove -y wget ca-certificates && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
VOLUME /var/lib/proxysql  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--", "proxysql", "-f"]  

