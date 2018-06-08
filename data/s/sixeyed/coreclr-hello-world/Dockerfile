FROM sixeyed/coreclr-base:1.0.0-rc1-final  
MAINTAINER Elton Stoneman <elton@sixeyed.com>  
  
# ensure the expected DNX is available  
ENV PATH /root/.dnx/runtimes/dnx-coreclr-linux-x64.1.0.0-rc1-final/bin:$PATH  
  
# deploy the Hello World app  
COPY /hello-world /opt/hello-world  
RUN cd /opt/hello-world && dnu restore  
  
CMD cd /opt/hello-world && dnx run

