FROM phusion/baseimage  
MAINTAINER Library Simplified <info@librarysimplified.org>  
  
ARG version  
ARG repo="NYPL-Simplified/circulation"  
ENV SIMPLIFIED_DB_TASK "auto"  
ENV TZ=US/Eastern  
  
# Copy over all Library Simplified build files for this image  
COPY . /ls_build  
  
RUN /bin/bash -c "/ls_build/simplified_app.sh ${repo} ${version} \  
&& /ls_build/logrotate.sh \  
&& /ls_build/simplified_cron.sh \  
&& rm -rf /ls_build && /bd_build/cleanup.sh"  
  
VOLUME /var/log  
WORKDIR /home/simplified/circulation/bin  
  
CMD ["/sbin/my_init"]  

