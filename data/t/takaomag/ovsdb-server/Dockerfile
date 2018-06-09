# takaomag/ovsdb-server  
FROM takaomag/openvswitch:release-2.7.0-2017.06.05.04.05  
ENV \  
X_DOCKER_REPO_NAME=ovsdb-server  
  
EXPOSE \  
6640  
VOLUME ["/run/openvswitch"]  
  
ENTRYPOINT ["/usr/sbin/ovsdb-server"]  
CMD ["--remote=punix:/run/openvswitch/db.sock", "--remote=ptcp:6640"]  

