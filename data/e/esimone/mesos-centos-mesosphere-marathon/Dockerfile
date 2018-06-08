FROM esimone/mesos-centos-mesosphere-base  
  
RUN yum install -y java marathon \  
&& yum --enablerepo=* clean all \  
&& rm -rf /var/cache/yum  
  
RUN /bin/mkdir -p /run/marathon \  
&& /bin/chown marathon:marathon /run/marathon \  
&& /bin/chmod 755 /run/marathon \  
&& sed -i '$d' /usr/share/marathon/bin/marathon \  
&& echo '[[ -f /etc/default/marathon ]] && source /etc/default/marathon'
>>/usr/share/marathon/bin/marathon \  
&& echo 'run "$@"' >>/usr/share/marathon/bin/marathon  
  
WORKDIR /usr/share/marathon  
  
USER marathon  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/share/marathon/bin/marathon"]  

