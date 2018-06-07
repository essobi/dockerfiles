FROM ubuntu:zesty  
LABEL maintainer "j"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# && apt-get install -y --force-yes --no-install-recommends \  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
motion=4.0-1 \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# 20 camera feeds max (by default Motion will use port 8080 and +1 for each
camera feed)  
EXPOSE 8080-8100  
CMD [ "motion", "-n" ]  
  

