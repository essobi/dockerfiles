FROM java:7  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup apt tools and other goodies we want  
RUN apt-get update && apt-get -y install --no-install-recommends octave && yes
Yes, do as I say! | apt-get purge --force-yes bash && apt-get -y autoremove &&
rm -f /bin/sh  
  
ADD smell-baron /bin/smell-baron  
ENTRYPOINT ["/bin/smell-baron"]  
CMD ["/usr/bin/octave" ]  

