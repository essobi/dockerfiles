# takaomag/ovs-vswitchd  
  
# Required docker options:  
# \--cap-add=NET_ADMIN  
# \--net host  
# \--volumes-from x-ovsdb-server  
# required volumes: /run/openvswitch  
  
FROM takaomag/openvswitch:release-2.7.0-2017.06.05.04.05  
  
ENV \  
X_DOCKER_REPO_NAME=ovs-vswitchd  
  
ENTRYPOINT ["/usr/sbin/ovs-vswitchd"]  
  

