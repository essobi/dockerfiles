FROM debian:stretch-slim as ovs_builder  
  
RUN apt-get update -q && apt-get install -q -y wget \  
gcc make \  
perl \  
python-pip \  
git \  
autoconf libtool libcap-ng-dev  
  
RUN pip install six  
  
ENV OPENVSWITCH_VERSION v2.9.0  
RUN git clone https://github.com/openvswitch/ovs.git && \  
cd ovs && \  
git checkout tags/$OPENVSWITCH_VERSION  
  
WORKDIR /ovs  
RUN ./boot.sh  
RUN ./configure  
RUN make  
RUN make DESTDIR=/tarball install  
  
FROM debian:stretch-slim  
RUN apt-get update -q && apt-get install -q -y libatomic1  
COPY \--from=ovs_builder /tarball /  
RUN mkdir -p /usr/local/var/run/openvswitch  
RUN ovsdb-tool create /usr/local/etc/openvswitch/ovnnb_db.db
/usr/local/share/openvswitch/ovn-nb.ovsschema  
RUN ovsdb-tool create /usr/local/etc/openvswitch/ovnsb_db.db
/usr/local/share/openvswitch/ovn-sb.ovsschema  
RUN ovsdb-tool create /usr/local/etc/openvswitch/conf.db
/usr/local/share/openvswitch/vswitch.ovsschema  
ENTRYPOINT ["ovsdb-server"]

