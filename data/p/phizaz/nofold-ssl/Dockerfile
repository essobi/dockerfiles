FROM phizaz/sklearn:python2  
MAINTAINER Konpat Preechakul <the.akita.ta@gmail.com>  
  
# install infernal for cmscore  
ENV infernal infernal-1.0.2  
RUN mkdir -p /tmp \  
&& cd /tmp \  
&& curl -O http://eddylab.org/software/infernal/${infernal}.tar.gz \  
&& tar -xzf ${infernal}.tar.gz \  
&& cd ${infernal} \  
&& ./configure \  
&& make && make install \  
&& rm -rf /tmp/*  
  
RUN pip install --no-cache-dir biopython  
RUN pip install --no-cache-dir fastcluster  
RUN pip install --no-cache-dir sortedcontainers  
RUN pip install --no-cache-dir future  
RUN pip install --no-cache-dir matplotlib  

