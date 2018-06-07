FROM mazaclub/dashpay-base  
# IMAGE mazaclub/electrum-dash-server:dash  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
EXPOSE 50001 50002 8000  
VOLUME ["/home/coin","/var/electrum-dash-server"]  
ENTRYPOINT ["/sbin/my_init"]  
  
ENV COIND localhost  
  
ADD . /  
  
RUN export GIT_BRANCH=$(cat .branch)  
# In Order for the build to work correctly, the branch in  
# docker-electrum-dash-server must match the branch in electrum-dash-server  
RUN apt-get update \  
&& apt-get install -y \  
apg python-dev python2.7 python-pip \  
git libleveldb1 libleveldb-dev  
  
RUN echo "bitcoin hard nofile 65536" >> /etc/security/limits.conf \  
&& echo "bitcoin soft nofile 65536" >> /etc/security/limits.conf \  
&& cd / \  
&& git clone https://github.com/dashpay/electrum-dash-server \  
&& cd /electrum-dash-server \  
&& echo ${GIT_BRANCH} \  
&& git checkout $(cat /.branch) \  
&& python setup.py install \  
&& mkdir -pv /app \  
&& cp -av /electrum-dash-server/* /app \  
&& rm -rf /electrum-dash-server/* \  
&& rm -rf /etc/service/sshd  
  
RUN chmod +x /etc/service/electrum-server/run  

