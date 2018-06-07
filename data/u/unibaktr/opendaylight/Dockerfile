FROM opendaylight/odl:4.2.0  
MAINTAINER Marcel Grossmann <whatever4711@gmail.com>  
LABEL architecture="amd64"  
  
# Need to install feature:install odl-restconf odl-l2switch-switch odl-mdsal-
apidocs odl-dlux-core  
WORKDIR /opt/opendaylight  
RUN sed -i '/^featuresBoot=/ s/$/,odl-dlux-core,odl-l2switch-switch,odl-
restconf,odl-mdsal-apidocs,odl-dlux-node,odl-dlux-yangui,odl-dlux-
yangvisualizer,odl-dlux-all/' etc/org.apache.karaf.features.cfg  
  
EXPOSE 162 179 1088 1790 1830 2400 2550 2551 2552 4189 4342 5005 5666 6633
6640 6653 7800 8000 8080 8101 8181 8383 12001  
ENTRYPOINT ["./bin/karaf", "server"]  

