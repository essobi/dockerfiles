# based on solita/ubuntu-systemd:16.04 and https://github.com/sjwl/docker-hub-
images/blob/master/maas/Dockerfile  
FROM ubuntu:16.10  
ENV container docker  
  
COPY setup.sh /setup.sh  
RUN /bin/bash setup.sh  
  
CMD ["/lib/systemd/systemd", "--log-target=journal", "--log-level=info"]  
  
# maas createadmin --username=root --password=welcome1 --email=foo@foo.com  

