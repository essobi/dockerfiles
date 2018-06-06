FROM ubuntu:14.04  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:vbernat/haproxy-1.5 && \  
apt-get update && apt-get install -y haproxy && \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy  
RUN apt-get update && apt-get install -y python python-dev python-pip && pip
install requests  
  
ADD run.py run.py  
  
EXPOSE 80  
EXPOSE 443  
  
CMD python run.py  

