FROM ubuntu:14.04  
MAINTAINER wenzizone <wenzizone@126.com>  
  
ADD init-fake.conf /etc/init/fake-container-events.conf  
  
# undo some leet hax of the base image  
RUN rm /usr/sbin/policy-rc.d; \  
rm /sbin/initctl; dpkg-divert --rename \--remove /sbin/initctl  
  
# generate a nice UTF-8 locale for our use  
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
  
# remove some pointless services  
RUN /usr/sbin/update-rc.d -f ondemand remove; \  
for f in \  
/etc/init/u*.conf \  
/etc/init/mounted-dev.conf \  
/etc/init/mounted-proc.conf \  
/etc/init/mounted-run.conf \  
/etc/init/mounted-tmp.conf \  
/etc/init/mounted-var.conf \  
/etc/init/hostname.conf \  
/etc/init/networking.conf \  
/etc/init/tty*.conf \  
/etc/init/plymouth*.conf \  
/etc/init/hwclock*.conf \  
/etc/init/module*.conf\  
; do \  
dpkg-divert --local \--rename \--add "$f"; \  
done; \  
echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab  
  
# prepare for takeoff  
CMD ["/sbin/init"]

