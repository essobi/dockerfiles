# Do not import the latest image. It will not run on eru.  
FROM kong:0.10  
  
RUN yum install -y git unzip  
RUN git config \--global url."https://".insteadOf git://  
RUN luarocks install kong-oidc  

