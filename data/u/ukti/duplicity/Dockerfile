FROM ubuntu:16.04  
# Set HOME to suppress warnings  
ENV HOME /root  
  
# For debconf not to complain  
ENV DEBIAN_FRONTEND noninteractive  
  
# force-unsafe-io to disable sync - safe for image building  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
apt-get update -y && \  
apt-get install -y ntpdate inotify-tools && \  
apt-get install -y python-pip awscli && \  
apt-get clean && apt-get autoremove && \  
rm -rf /var/lib/cache/* /var/lib/log/* /tmp/* /var/tmp/*  
  
RUN apt-get install -y librsync-dev  
ADD
https://code.launchpad.net/duplicity/0.7-series/0.7.10/+download/duplicity-0.7.10.tar.gz
/tmp  
RUN pip install /tmp/duplicity-0.7.10.tar.gz boto urllib3  
  
ADD /root /  
RUN chmod a+x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  
#container parameters  
ENV AWS_ACCESS_KEY_ID tbd  
ENV AWS_SECRET_ACCESS_KEY tbd  
ENV DUPLICITY_ARGS "--s3-use-new-style --s3-european-buckets"  

