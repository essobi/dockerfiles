FROM python:3.6-alpine  
LABEL maintainer="Josh Dvir - josh@dvir.uk" \  
io.whalebrew.name="cfn-flip"  
  
RUN mkdir -p /workdir  
WORKDIR /workdir  
  
RUN pip install cfn_flip  
  
ENTRYPOINT ["cfn-flip"]  

