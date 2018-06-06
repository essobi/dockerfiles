FROM dit4c/dit4c-container-x11:xpra  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
RUN SLICER_URL="http://download.slicer.org/bitstream/461634" && \  
curl -v -s -L $SLICER_URL | tar xz -C /tmp && \  
mv /tmp/Slicer* /opt/slicer  
  
# See http://na-mic.org/Mantis/view.php?id=4015  
RUN su researcher -c "mkdir /home/researcher/Documents"  
  
RUN yum install -y mesa-libGLU  
  
COPY /etc /etc  
COPY /opt /opt  
  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /opt/slicer/slicer.desktop"
/etc/tint2/panel.tint2rc  

