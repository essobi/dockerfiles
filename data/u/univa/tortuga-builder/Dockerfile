FROM centos:7  
# Python 3.6 and other build tools  
RUN rpm -ivh http://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm
&& \  
yum install -y centos-release-scl puppet-agent && \  
yum install -y rh-python36 git rsync bzip2 && \  
rm -rf /var/cache/yum && \  
. /opt/rh/rh-python36/enable && \  
pip install tox  
  
# Fix buggy pip  
RUN . /opt/rh/rh-python36/enable && \  
pip install --upgrade
"git+https://github.com/EmmEff/pip2pi.git@pip-10-fix#egg=pip2pi-0.7.0"  
  
# Make sure the environment is set up right  
ADD scripts/entrypoint.sh /  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
# Support running builds like so:  
# docker run -it --rm -v `pwd`:/tortuga univa/tortuga-builder  
WORKDIR /tortuga  
CMD [ "bash", "-c", "pip install -r requirements.txt && paver build" ]  

