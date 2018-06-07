FROM ubuntu:14.04.4  
ENV TARGET_DIR /data  
ENV GIT_BRANCH master  
ENV MAKECATALOGS false  
ENV FAT_VERSION 0.5.0  
# Install git  
RUN apt-get update \  
&& mkdir -p /usr/local/bin \  
&& apt-get install -y curl git rsync \  
&& curl -sLO https://github.com/cyaninc/git-fat/archive/${FAT_VERSION}.tar.gz
\  
&& tar xzf /${FAT_VERSION}.tar.gz -C / \  
&& mv /git-fat-${FAT_VERSION}/git_fat/git_fat.py /usr/local/bin/git-fat \  
&& chmod 755 /usr/local/bin/git-fat \  
&& git clone https://github.com/munki/munki.git \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /git-fat-${FAT_VERSION} \  
&& rm -rf /${FAT_VERSION}.tar.gz  
  
# Configure .ssh directory  
RUN mkdir /root/.ssh \  
&& chmod 0600 /root/.ssh \  
&& echo StrictHostKeyChecking no > /root/.ssh/config  
  
# Configure entrypoint  
COPY /docker-entrypoint.sh /  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
RUN chmod 755 /docker-entrypoint.sh && chmod -R 755 /docker-entrypoint.d  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

