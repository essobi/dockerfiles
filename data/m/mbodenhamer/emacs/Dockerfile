FROM mbodenhamer/emacs:latest  
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>  
  
# Provision custom setup  
ONBUILD ARG provision=provision.sh  
ONBUILD COPY $provision /root/provision.sh  
ONBUILD RUN chmod +x /root/provision.sh \  
&& sync \  
&& /root/provision.sh \  
&& rm /root/provision.sh  
  
# Run emacs installation script  
ONBUILD ARG packages=packages.el  
ONBUILD COPY $packages /root/packages.el  
ONBUILD RUN emacs --batch -l /root/packages.el \  
&& rm /root/packages.el  
  
# Upload custom emacs file  
ONBUILD ARG conf=.emacs  
ONBUILD COPY $conf /root/.emacs  
  
# Set up emacs user  
ONBUILD ARG uid=1000  
ONBUILD ARG gid=1000  
ONBUILD RUN groupadd -g $gid user \  
&& useradd -u $uid -g $gid -d /home/user -m -s /bin/bash user \  
&& cp /root/.emacs /home/user \  
&& cp -r /root/.emacs.d /home/user \  
&& chown -R $uid:$gid /home/user  
ONBUILD USER user  

