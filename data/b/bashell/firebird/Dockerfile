FROM centos:7  
MAINTAINER Chaiwat Suttipongsakul "cwt@bashell.com"  
ENV RELEASE=3.0.2  
ENV BUILD=32703-0  
ENV ARCH=amd64  
ENV MIRROR_URL=https://jaist.dl.sourceforge.net/project/firebird/firebird-
linux-$ARCH/$RELEASE-Release/Firebird-$RELEASE.$BUILD.$ARCH.tar.gz  
  
WORKDIR /  
  
RUN yum update && yum upgrade -y \  
&& yum install -y epel-release \  
&& yum install -y libtommath libicu \  
&& yum clean all  
  
RUN curl $MIRROR_URL | tar zxf - \  
&& tar zxf Firebird-$RELEASE.$BUILD.$ARCH/buildroot.tar.gz \  
&& rm -rf Firebird-$RELEASE.$BUILD.$ARCH \  
&& mkdir /data \  
&& mv /opt/firebird/security3.fdb /data \  
&& mkdir /data/example \  
&& mv /opt/firebird/examples/empbuild/employee.fdb /data/example \  
&& chmod 644 /data/example/employee.fdb \  
&& sed -i -e 's/^#SecurityDatabase.*security3.fdb$/SecurityDatabase =
\/data\/security3.fdb/' /opt/firebird/firebird.conf \  
&& sed -i -e 's/^#DatabaseAccess.*Full$/DatabaseAccess = Restrict \/data/'
/opt/firebird/firebird.conf \  
&& sed -i -e 's/^#RemoteAccess.*true$/RemoteAccess = true/'
/opt/firebird/firebird.conf \  
&& sed -i -e 's/^#RemoteFileOpenAbility.*0$/RemoteFileOpenAbility = 1/'
/opt/firebird/firebird.conf \  
&& sed -i -e 's/^#WireCrypt.*server)$/WireCrypt = Enabled/'
/opt/firebird/firebird.conf \  
&& sed -i -e 's/^#ServerMode.*Super$/ServerMode = Super/'
/opt/firebird/firebird.conf \  
&& sed -i -e 's/\$(dir_sampleDb)/\/data\/example/g'
/opt/firebird/databases.conf \  
&& sed -i -e 's/\$(dir_secDb)/\/data/g' /opt/firebird/databases.conf \  
&& /opt/firebird/bin/gsec -add sysdba -pw masterkey  
  
ADD start_firebird.sh /  
  
EXPOSE 3050/tcp  
VOLUME /data  
ENTRYPOINT ["/start_firebird.sh"]  

