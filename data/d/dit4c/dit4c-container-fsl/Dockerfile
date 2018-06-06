FROM dit4c/dit4c-container-x11:debian  
  
RUN curl -sL http://neuro.debian.net/lists/jessie.au.full | \  
tee /etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9  
  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y fsl-core  
  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/fslview.desktop"
/etc/tint2/panel.tint2rc && \  
sed -i "${LNUM}ilauncher_item_app =
/usr/share/applications/fsl-5.0-core.desktop" /etc/tint2/panel.tint2rc  

