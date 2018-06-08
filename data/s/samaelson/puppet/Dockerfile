FROM alpine:edge  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing/ >>
/etc/apk/repositories \  
&& apk add \--update-cache shadow ruby less bash pylint git ruby-json\  
&& gem install puppet yaml-lint puppet-lint --no-rdoc --no-ri \  
&& mkdir -p /opt/puppetlabs/bin && ln -s $(which puppet)
/opt/puppetlabs/bin/puppet  
CMD ["/bin/ash"]  

