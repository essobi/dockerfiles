FROM debian:unstable  
SHELL ["/bin/bash", "-c"]  
  
RUN apt-get update && apt-get install -yq --no-install-recommends wget
default-jre \  
&& rm -rf /tmp/* /var/{tmp,cache}/* /var/lib/{apt,dpkg}/  
  
RUN adduser --disabled-password user --gecos "User"  
USER user  
ENV HOME /home/user  
ENV PULSE_SERVER unix:/tmp/pulse  
  
RUN cd ; wget
http://raccoon.onyxbits.de/sites/raccoon.onyxbits.de/files/raccoon-4.1.0.jar  
  
CMD ["java","-jar","/home/user/raccoon-4.1.0.jar"]  

