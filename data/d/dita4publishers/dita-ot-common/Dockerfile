FROM ditacommunity/dita-ot-base:1.8.5  
#  
# Sets up a DITA-OT container  
# with all of the DITA for Publishers  
# open toolkit plugins integrated.  
WORKDIR ${DITA_HOME}  
ENV DITA_COMM_URL=https://github.com/dita4publishers/ BRANCH=develop  
#  
# Common plugins needed by all transforms:  
#  
RUN wget ${DITA_COMM_URL}org.dita4publishers.common.html/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.common.html-${BRANCH}
plugins/org.dita4publishers.common.html && rm ${BRANCH}.zip && \  
wget
${DITA_COMM_URL}org.dita4publishers.common.mapdriven/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.common.mapdriven-${BRANCH}
plugins/org.dita4publishers.common.mapdriven && rm ${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita4publishers.common.xslfo/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.common.xslfo-${BRANCH}
plugins/org.dita4publishers.common.xslfo && rm ${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita4publishers.common.xslt/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.common.xslt-${BRANCH}
plugins/org.dita4publishers.common.xslt && rm ${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita4publishers.math-d.html/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.math-d.html-${BRANCH}
plugins/org.dita4publishers.math-d.html && rm ${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita4publishers.media-d.html/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita4publishers.media-d.html-${BRANCH}
plugins/org.dita4publishers.media-d.html && rm ${BRANCH}.zip  
#  
# Integrate new plugins  
#  
RUN ant -f integrator.xml  
#  
# End of Dockerfile  
#  
  

