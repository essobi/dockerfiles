# Copyright (c) General Electric Company, 2017. All rights reserved.  
FROM rt106/rt106-algorithm-sdk  
  
USER root  
  
RUN apt-get -y update \  
&& apt-get -y install python-dev python-tk libgtk2.0-0 gcc libxft-dev
libfreetype6 libfreetype6-dev \  
&& pip install opencv-python \  
&& pip install numpy scipy matplotlib  
  
ADD *.py /rt106/  
ADD rt106SpecificAdaptorDefinitions.json
/rt106/rt106SpecificAdaptorDefinitions.json  
ADD entrypoint.sh /rt106/entrypoint.sh  
  
RUN mkdir -p /rt106/input && mkdir -p /rt106/output  
  
RUN chmod a+x /rt106/entrypoint.sh  
  
WORKDIR /rt106  
RUN chown -R rt106:rt106 /rt106  
USER rt106:rt106  
  
CMD ["/rt106/entrypoint.sh"]  

