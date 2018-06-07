FROM ceph/base  
MAINTAINER Dmitry Karpov "d.p.karpov@gmail.com"  
RUN apt-get update \  
&& apt-get install -y runit tgt \  
&& apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
/var/tmp/* /tmp/*  
  
ADD ./service /etc/service  
#ADD ./my_init.d /etc/my_init.d  
ADD my_init/my_init /sbin/my_init  
ADD 2.sh /etc/runit/2  
ADD ./tpl.confd /tpl.confd  
  
RUN chmod +x \  
/sbin/my_init \  
/etc/runit/2 \  
&& mkdir -p \  
/etc/container_environment \  
/etc/my_init.d \  
&& find /etc/service -name "run" | xargs chmod +x  
#&& find /etc/my_init.d -name "*.sh" | xargs chmod +x  
CMD ["/sbin/my_init"]

