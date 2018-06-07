FROM maza/maza-core-daemon  
#FROM mazaclub/mazacoind-base  
# IMAGE mazaclub/encompass-mercury:mzc  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
EXPOSE 50001 50002 8000  
VOLUME ["/home/coin","/var/encompass-mercury"]  
ENTRYPOINT ["/sbin/my_init"]  
  
ENV COIND localhost  
  
ADD . /  
  
RUN export GIT_BRANCH=$(git symbolic-ref --short -q HEAD)  
# In Order for the build to work correctly, the branch in  
# docker-encompass-mercury must match the branch in encompass-mercury  
RUN apt-get update \  
&& apt-get install -y \  
apg python-dev python2.7 python-pip \  
git libleveldb1 libleveldb-dev  
RUN pip install --upgrade six  
RUN echo "bitcoin hard nofile 65536" >> /etc/security/limits.conf \  
&& echo "bitcoin soft nofile 65536" >> /etc/security/limits.conf \  
&& cd / \  
&& git clone https://github.com/mazaclub/encompass-mercury \  
&& cd /encompass-mercury \  
&& git checkout ${GIT_BRANCH} \  
&& python setup.py install --force \  
&& mkdir -pv /app \  
&& mv /encompass-mercury/* /app \  
&& rm -rf /etc/service/sshd  
  
RUN chmod +x /etc/service/encompass-mercury/run  

