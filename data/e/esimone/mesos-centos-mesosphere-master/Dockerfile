FROM esimone/mesos-centos-mesosphere-base  
  
EXPOSE 5050  
ENTRYPOINT ["/usr/bin/mesos-init-wrapper", "master"]  
  
CMD ["--registry=in_memory"]  

