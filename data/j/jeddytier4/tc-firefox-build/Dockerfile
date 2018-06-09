FROM tatsushid/tinycore:6.3-x86_64  
  
# Instructions are run with 'tc' user  
RUN tce-load -wic \  
firefox \  
&& cd /tmp/tce/optional \  
&& for PKG in `ls *.tcz`; do \  
echo "Removing $PKG files"; \  
for F in `unsquashfs -l $PKG | grep squashfs-root | sed -e 's/squashfs-
root//'`; do \  
[ -f $F -o -L $F ] && sudo rm -f $F; \  
done; \  
INSTALLED=$(echo -n $PKG | sed -e s/.tcz//); \  
sudo rm -f /usr/local/tce.installed/$INSTALLED; \  
done \  
&& sudo rm -f /usr/bin/file \  
&& sudo /sbin/ldconfig \  
&& rm -rf /tmp/tce/optional/* \  
  
# Instructions after here are run with 'root' user  
# USER root  
CMD ["/bin/sh"]

