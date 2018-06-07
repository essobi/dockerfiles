FROM python:3.5-onbuild  
RUN git clone https://github.com/D-I-L/pydgin.git  
RUN sed -i '/^mod-wsgi==/ d' pydgin/requirements-dev.txt  
RUN sed -i "s|'mod_wsgi.server',||" pydgin/pydgin/settings.py  
RUN pip install --no-cache-dir -r pydgin/requirements.txt  
RUN mkdir /usr/src/app/pydgin/log/  
RUN mkdir /usr/src/app/tcell/  
#  
# setup JBrowse  
RUN apt-get update && apt-get install -y \  
unzip \  
wget \  
make \  
&& rm -rf /var/lib/apt/lists/*  
RUN wget -O /usr/src/app/JBrowse-1.12.1.zip "http://jbrowse.org/wordpress/wp-
content/plugins/download-monitor/download.php?id=105"  
RUN unzip /usr/src/app/JBrowse-1.12.1.zip -d /usr/src/app/  
RUN rm -f /usr/src/app/JBrowse-1.12.1.zip  
RUN cd /usr/src/app/JBrowse-1.12.1 && ./setup.sh  
RUN mkdir /usr/src/app/JBrowse-1.12.1/data  
RUN git clone https://github.com/cmdcolin/gwasviewer.git
/usr/src/app/JBrowse-1.12.1/plugins/GWASViewer  
RUN git clone https://github.com/tottlefields/jbrowse-pydginelastic.git
/usr/src/app/JBrowse-1.12.1/plugins/PydginElastic  
RUN mkdir /usr/src/app/pydgin/pydgin/apache  
RUN ln -s /usr/src/app/JBrowse-1.12.1/
/usr/src/app/pydgin/pydgin/apache/jbrowse  
RUN ln -s /usr/src/app/tcell/ /usr/src/app/pydgin/pydgin/apache/tcell  
WORKDIR /usr/src/app/pydgin  

