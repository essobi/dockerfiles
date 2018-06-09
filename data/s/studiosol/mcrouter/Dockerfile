FROM ubuntu:14.04  
  
ENV MCROUTER_VERSION 0.19.0  
ENV MCROUTER_DIR /  
  
RUN apt-get update && apt-get install -y wget && apt-get clean && rm -rf
/var/lib/apt/lists  
  
RUN wget -qO-
https://github.com/facebook/mcrouter/archive/v${MCROUTER_VERSION}.tar.gz | tar
xvz -C /  
RUN /mcrouter-${MCROUTER_VERSION}/mcrouter/scripts/install_ubuntu_14.04.sh
/mcrouter-${MCROUTER_VERSION}/ \  
&& rm -rf /var/lib/apt/lists &&
/mcrouter-${MCROUTER_VERSION}/mcrouter/scripts/clean_ubuntu_14.04.sh
/mcrouter-${MCROUTER_VERSION}/  
RUN mv /mcrouter-0.19.0/install/bin/mcrouter /usr/bin  
  
CMD ["mcrouter"]  
  

