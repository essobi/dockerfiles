#  
# Dockerfile for the mencoder.  
#  
# Robert Haines.  
#  
# BSD Licenced. See LICENCE for details.  
#  
FROM ubuntu:14.04  
MAINTAINER Robert Haines <robert.haines@manchester.ac.uk>  
  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -qy \  
mencoder \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV HOME /home/mencoder  
RUN useradd --create-home --home-dir $HOME \--gid users mencoder \  
&& mkdir -p $HOME/video \  
&& chown -R mencoder:users $HOME  
  
WORKDIR $HOME/video  
USER mencoder  
  
ENTRYPOINT ["mencoder"]  
CMD ["-list-options"]  

