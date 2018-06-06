FROM dit4c/dit4c-container-x11:debian-xpra  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
RUN echo "deb http://qgis.org/debian/ jessie main" >> /etc/apt/sources.list &&
\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-key 3FF5FFCAD71472C4  
  
RUN apt-get update && \  
apt-get install -y qgis python-pip python-all-dev && \  
apt-get clean  
  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/qbrowser.desktop"
/etc/tint2/panel.tint2rc && \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/qgis.desktop"
/etc/tint2/panel.tint2rc  
  
RUN pip install ipython jupyter  
  
COPY etc /etc  
COPY var /var  
  
RUN su - researcher -c "mkdir -p ~/.jupyter && echo \"c.NotebookApp.base_url =
'/jupyter'\" > ~/.jupyter/jupyter_notebook_config.py"  

