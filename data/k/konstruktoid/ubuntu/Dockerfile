  
FROM scratch  
ADD ./yakkety-1612102231.txz /  
ENV SHA 9ea24dd8101e1f7ed2fe7ec72cc911706ab50aa4ea7fdadbcc17574735432754  
  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
ONBUILD RUN apt-get update && apt-get -y upgrade  
  

