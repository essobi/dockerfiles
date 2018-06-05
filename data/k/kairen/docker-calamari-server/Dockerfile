FROM ubuntu:14.04  
MAINTAINER Kyle.Bai <kyle.b@inwinstack.com>  
  
USER root  
  
RUN apt-get update && apt-get install -y curl expect  
RUN sudo apt-key del 17ED316D  
RUN curl https://git.ceph.com/release.asc | sudo apt-key add -  
RUN echo "deb http://download.ceph.com/calamari/1.3.1/ubuntu/trusty trusty
main" | sudo tee /etc/apt/sources.list.d/calamari.list  
RUN apt-get update  
RUN apt-get install -y salt-minion salt-master diamond  
RUN mv /etc/diamond/diamond.conf.example /etc/diamond/diamond.conf  
RUN service salt-master restart | service diamond restart  
RUN apt-get install -y calamari-server calamari-clients  
  
COPY initialize /opt/initialize  
  
COPY boot_run.sh /etc/boot_run.sh  
RUN chown root.root /etc/boot_run.sh  
RUN chmod 700 /etc/boot_run.sh  
  
EXPOSE 80/tcp 4505/tcp 4506/tcp  
  
  
ENTRYPOINT ["/etc/boot_run.sh"]  
  

