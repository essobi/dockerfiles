# This is designed to be run from fig as part of a  
# Marketplace development environment.  
# NOTE: this is not provided for production usage.  
FROM mozillamarketplace/centos-python27-mkt:0.6  
RUN yum install -y supervisor  
  
RUN mkdir -p /pip/{cache,build}  
  
ADD requirements /pip/requirements  
  
RUN sed -i 's/M2Crypto.*$/# Removed in favour of packaged version/'
/pip/requirements/compiled.txt  
  
# Setting cwd to /pip ensures egg-links for git installed deps are created in
/pip/src  
WORKDIR /pip  
# Because websigning is annoying.  
RUN pip install nose==1.3.4  
RUN pip install -b /pip/build --download-cache /pip/cache --no-deps -r
/pip/requirements/dev.txt  
  
EXPOSE 2606  

