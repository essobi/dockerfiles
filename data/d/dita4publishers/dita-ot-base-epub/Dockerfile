FROM dita4publishers/dita-ot-common:1.8.5  
#  
# Sets up a DITA-OT container  
# with just the EPUB transform.  
# open toolkit plugins integrated.  
WORKDIR ${DITA_HOME}  
ENV DITA_COMM_URL=https://github.com/dita4publishers/ BRANCH=develop  
#  
# Legacy sourceforge doctypes support:  
#  
RUN wget
${DITA_COMM_URL}net.sourceforge.dita4publishers.doctypes/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d plugins && mv
plugins/net.sourceforge.dita4publishers.doctypes-${BRANCH}
plugins/net.sourceforge.dita4publishers.doctypes && rm ${BRANCH}.zip  
#  
# All plugins  
#  
RUN wget ${DITA_COMM_URL}org.dita4publishers.epub/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.epub-${BRANCH} plugins/org.dita4publishers.epub &&
rm ${BRANCH}.zip  
#  
# Integrate new plugins  
#  
RUN ant -f integrator.xml  
#  
# End of Dockerfile  
#  

