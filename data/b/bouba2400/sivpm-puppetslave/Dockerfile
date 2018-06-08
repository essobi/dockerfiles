FROM bouba2400/sivpm-baseos:1.0.0  
RUN curl -o puppet.deb -s https://apt.puppetlabs.com/puppetlabs-release-
pc1-trusty.deb && \  
DEBIAN_FRONTEND=noninteractive dpkg -i puppet.deb > /dev/null && \  
rm puppet.deb  
  
RUN apt-get update -q 2 && \  
DEBIAN_FRONTEND=noninteractive apt-get install --yes -q 2 puppet-agent  
  
RUN mkdir /etc/service/puppetagent  
COPY start-puppetagent.sh /etc/service/puppetagent/run  
RUN dos2unix /etc/service/puppetagent/run  
RUN chmod +x /etc/service/puppetagent/run  
  
#RUN ln -s /opt/puppetlabs/bin/puppet /usr/local/bin/puppet  
ENV PATH=/opt/puppetlabs/bin/:$PATH  
  
CMD ["/sbin/my_init"]  

