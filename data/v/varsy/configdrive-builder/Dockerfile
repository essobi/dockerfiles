FROM varsy/centos6-utils  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
RUN yum install -y genisoimage  
ADD runner /runner  
RUN chmod +x /runner  
  
CMD /runner  

