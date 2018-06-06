# Dockerfile for Gephi graph image manipulation software  
FROM dit4c/dit4c-container-x11:latest  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
USER root  
  
RUN rpm --rebuilddb && yum install -y java-1.8.0-openjdk-devel  
  
# Install Gephi, remove unnecessary files and symlink the binary into the path  
RUN curl -L -s
https://github.com/gephi/gephi/releases/download/v0.9.0/gephi-0.9.0-linux.tar.gz
| tar xzvC /opt && \  
find /opt/gephi* \\( -name "*.dll" -or -name "*.exe" \\) -exec rm -f {} \; &&
\  
ln -s /opt/gephi*/bin/gephi /usr/local/bin/gephi  
  
COPY gephi.desktop /usr/share/applications/  
  
RUN cd /tmp/ && curl -LO -s
https://raw.githubusercontent.com/gephi/gephi/master/modules/application/src/main/app-
resources/gephi48.png && \  
mv gephi48.png /usr/share/icons/gnome/48x48/apps/ && \  
rm /usr/share/applications/java*  
  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/gephi.desktop"
/etc/tint2/panel.tint2rc  

