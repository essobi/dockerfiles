FROM ubuntu:trusty  
  
RUN apt-get update && \  
apt-get install -y python-requests python-boto && \  
apt-get clean  
  
RUN useradd --no-create-home runner  
  
USER runner  
  
ADD bin/elb-presence /bin/elb-presence  
  
CMD /bin/elb-presence  

