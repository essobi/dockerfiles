FROM debian:stretch-slim  
  
ENV LANG=C.UTF-8 USER=root HOME=/root  
  
# Tools for dockerfiles and image management  
COPY sbin /usr/local/sbin  
COPY apt.conf /etc/apt/apt.conf.d/apluslms  
RUN chmod 0555 /usr/local/sbin/*  
  
# Base tools that are used by all images  
RUN apt_install \  
runit \  
ca-certificates \  
curl \  
jo \  
git \  
openssh-client \  
python3-requests \  
&& cp /usr/bin/chpst /usr/local/bin \  
&& dpkg -P runit \  
&& (cd /usr/local/bin && ln -s chpst setuidgid && ln -s chpst softlimit && ln
-s chpst setlock)  
  
# Base grading tools  
COPY bin /usr/local/bin  
COPY grade-wrapper.sh /gw  
RUN mkdir -p /feedback /submission /exercise \  
&& chmod 0770 /feedback \  
&& chmod 0555 /gw /usr/local/bin/*  
  
# Base environment  
WORKDIR /submission  
ENTRYPOINT ["/gw"]  
CMD ["/exercise/run.sh"]  

