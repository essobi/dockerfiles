# DOCKER-VERSION 1.0  
FROM dit4c/dit4c-container-x11  
MAINTAINER t.dettrick@uq.edu.au  
  
RUN curl -s -L https://bintray.com/dit4c/el7/rpm > /etc/yum.repos.d/bintray-
dit4c-el7.repo  
  
# Install  
# - octave  
# - ghostscript for octave plots  
RUN rpm --rebuilddb && fsudo yum install -y \  
octave \  
ghostscript-devel  
  
RUN cd /tmp && \  
wget
"http://downloads.sourceforge.net/project/pstoedit/pstoedit/3.62/pstoedit-3.62.tar.gz"
&& \  
tar xzvf pstoedit-3.62.tar.gz && \  
cd pstoedit-3.62 && \  
./configure && \  
make && \  
make install && \  
cd .. && rm -r pstoedit-*  
  
RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1)
&& \  
sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/www.octave.org-
octave.desktop" /etc/tint2/panel.tint2rc  
  
RUN sed -i "s/^Icon=.*/Icon=octave/" /usr/share/applications/www.octave.org-
octave.desktop  

