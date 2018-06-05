FROM dit4c/dit4c-container-x11:latest  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
USER root  
  
RUN yum install -y mesa-libGLU bzip2  
  
RUN BLENDER_VERSION=blender-2.75a-linux-glibc211-x86_64 && \  
curl -L -s
http://mirror.cs.umn.edu/blender.org/release/Blender2.75/${BLENDER_VERSION}.tar.bz2
| tar xj -C /opt && \  
ln -s /opt/${BLENDER_VERSION} /opt/blender && \  
ln -s /opt/blender/blender /usr/local/bin/blender  
  
RUN git clone --depth 1 git://git.blender.org/blender.git /tmp/blender && \  
mv /tmp/blender/release/freedesktop/blender.desktop /usr/share/applications/
&& \  
rsync -av --remove-source-files /tmp/blender/release/freedesktop/icons/
/usr/share/icons/gnome/ && \  
rm -rf /tmp/blender  
  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/blender.desktop"
/etc/tint2/panel.tint2rc  

