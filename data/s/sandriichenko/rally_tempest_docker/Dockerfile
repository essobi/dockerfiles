FROM xrally/xrally-openstack:0.9.0  
MAINTAINER Sofiia Andriichenko <sandriichenko@mirantis.com>  
  
ENV TEMPEST_TAG="16.0.0"  
ENV DESIGNATE_TAG="0.2.0"  
ENV BARBICAN_TAG="95a7322ccdb1ae244093fa38e81c0ad730b69ef0"  
  
WORKDIR /var/lib  
USER root  
  
# TBD define plugins tag/branch and Ironic plugin  
  
RUN git clone https://github.com/openstack/tempest.git -b $TEMPEST_TAG && \  
pip install tempest==$TEMPEST_TAG && \  
pip install ddt==1.0.1 && \  
git clone https://github.com/openstack/designate-tempest-plugin.git -b
$DESIGNATE_TAG && \  
pip install -r designate-tempest-plugin/test-requirements.txt && \  
git clone https://github.com/openstack/barbican-tempest-plugin.git &&\  
pip install ansible==2.3  
  
WORKDIR /home/rally  
  
COPY mcp_skip.list /var/lib/mcp_skip.list  
COPY lvm_mcp.conf /var/lib/lvm_mcp.conf  
COPY run_tempest.sh /usr/bin/run-tempest  
COPY barbican_skip.patch /var/lib/barbican-tempest-plugin/barbican_skip.patch  
  
WORKDIR /var/lib/barbican-tempest-plugin  
  
RUN git checkout $BARBICAN_TAG && \  
pip install -r requirements.txt && \  
pip install -r test-requirements.txt  
  
ENV SOURCE_FILE keystonercv3  
  
ENTRYPOINT ["run-tempest"]  

