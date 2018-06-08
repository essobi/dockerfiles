FROM midonet/neutron:base  
MAINTAINER MidoNet (http://midonet.org)  
  
COPY conf/cloudarchive-ost.list /etc/apt/sources.list.d/cloudarchive-ost.list  
COPY conf/midonet-plugin.list /etc/apt/sources.list.d/midonet-plugin.list  
  
RUN apt-get install -qy ubuntu-cloud-keyring  
RUN apt-get -q update  
RUN apt-get install -qy --no-install-recommends \  
neutron-server \  
python-neutronclient \  
python-keystoneclient \  
python-networking-midonet \  
python-neutron-lbaas \  
python-neutron-fwaas \  
python-neutron-vpnaas  
  
RUN mv /midonet_conf/neutron-server /etc/default/neutron-server  
RUN mv /midonet_conf/neutron_lbaas.conf /etc/neutron/neutron_lbaas.conf  
RUN mv /midonet_conf/neutron_vpnaas.conf /etc/neutron/neutron_vpnaas.conf  
  

