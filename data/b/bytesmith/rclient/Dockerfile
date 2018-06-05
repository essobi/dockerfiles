FROM centos:7  
MAINTAINER info@bytesmith.de  
RUN yum clean all \  
&& cd /tmp \  
&& curl -O
https://rserverdistribution.azureedge.net/production/RClient/9.1.0.0/3551_rev/1033/246b4328439b435bb5171f59f7d17fb7/microsoft-
r-client-3.3.3.tar.gz \  
&& tar zxvf microsoft-r-client-3.3.3.tar.gz \  
&& cd /tmp/MRC_Linux \  
&& ./install.sh -a -s -m \  
&& rm -rf /tmp/MRC_Linux/ \  
&& rm -rf /tmp/microsoft-r-client-3.3.3.tar.gz  
ENTRYPOINT ["Revo64"]

