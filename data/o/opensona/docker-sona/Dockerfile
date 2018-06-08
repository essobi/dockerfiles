FROM onosproject/onos:latest as builder  
MAINTAINER Daniel Park <dan.park@sk.com>  
  
WORKDIR /root/onos  
RUN touch apps/org.onosproject.drivers/active && \  
touch apps/org.onosproject.openflow-base/active && \  
touch apps/org.onosproject.openstacknetworking/active  
  
EXPOSE 6653 6640 8181 8101 9876  
WORKDIR /root/onos  
  
# Get ready to run command  
ENTRYPOINT ["./bin/onos-service"]  
CMD ["server"]  

