FROM macadmins/puppetmaster  
  
MAINTAINER nmcspadden@gmail.com  
  
RUN yum install -y tar python-setuptools && yum clean all  
ADD https://github.com/kennethreitz/requests/tarball/master
/home/requests/master.tar.gz  
RUN tar -zxvf /home/requests/master.tar.gz --strip-components=1 -C
/home/requests && rm -f /home/requests/master.tar.gz  
WORKDIR /home/requests  
RUN python /home/requests/setup.py install  
ADD https://github.com/nmcspadden/WHD-CLI/tarball/master
/home/whdcli/master.tar.gz  
RUN tar -zxvf /home/whdcli/master.tar.gz --strip-components=1 -C /home/whdcli
&& rm /home/whdcli/master.tar.gz  
WORKDIR /home/whdcli  
RUN python /home/whdcli/setup.py install  
ADD puppet.conf /etc/puppet/puppet.conf  
ADD com.github.nmcspadden.whd-cli.plist
/home/whdcli/com.github.nmcspadden.whd-cli.plist  
ADD check_csr.py /etc/puppet/check_csr.py  
RUN touch /var/log/check_csr.out  
RUN chown puppet:puppet /var/log/check_csr.out  
  
RUN cp -Rfv /etc/puppet/ /opt/  
RUN cp -Rfv /var/lib/puppet/ /opt/varpuppet/lib/

