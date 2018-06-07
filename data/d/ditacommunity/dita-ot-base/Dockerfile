FROM ditaot/dita-ot-base:1.8.5  
#  
# Sets up a DITA-OT container  
# with all of the DITA Community  
# open toolkit plugins integrated.  
WORKDIR ${DITA_HOME}  
ENV DITA_COMM_URL=https://github.com/dita-community/ BRANCH=develop  
#  
# Common XSLT  
#  
RUN wget ${DITA_COMM_URL}org.dita-community.common.xslt/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-
community.common.xslt-${BRANCH} plugins/org.dita-community.common.xslt && rm
${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita-community.common.mapdriven/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-
community.common.mapdriven-${BRANCH} plugins/org.dita-
community.common.mapdriven && rm ${BRANCH}.zip && \  
#  
# PDF Flagging:  
# NOTE: This plugin requires a flagging preprocess extension that doesn't
exist in the 1.8.5 or earlier OTs.  
# RUN wget ${DITA_COMM_URL}org.dita-
community.pdf.flagging/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins
&& rm ${BRANCH}.zip  
#  
# PDF extensions  
#  
wget ${DITA_COMM_URL}org.dita-community.pdf-page-break/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-community.pdf-page-
break-${BRANCH} plugins/org.dita-community.pdf-page-break && rm ${BRANCH}.zip
&& \  
wget ${DITA_COMM_URL}org.dita-community.pdf-dl-as-dl/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-community.pdf-dl-as-
dl-${BRANCH} plugins/org.dita-community.pdf-dl-as-dl && rm ${BRANCH}.zip && \  
#  
# Preprocessing extensions: (Not yet working with OT 2.2.2)  
#  
wget ${DITA_COMM_URL}org.dita-community.adjust-copy-to/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-community.adjust-
copy-to-${BRANCH} plugins/org.dita-community.adjust-copy-to && rm
${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita-community.xhtml-adjct/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-community.xhtml-
adjct-${BRANCH} plugins/org.dita-community.xhtml-adjct && rm ${BRANCH}.zip &&
\  
wget ${DITA_COMM_URL}org.dita-community.preprocess-
extensions/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && mv
plugins/org.dita-community.preprocess-extensions-${BRANCH} plugins/org.dita-
community.preprocess-extensions && rm ${BRANCH}.zip && \  
#  
# Preprocess tester:  
#  
# RUN wget ${DITA_COMM_URL}org.dita-community.preprocess-
tester/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm
${BRANCH}.zip  
#  
# DITA Community doctypes  
#  
wget ${DITA_COMM_URL}org.dita-community.doctypes/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d plugins && mv plugins/org.dita-
community.doctypes-${BRANCH} plugins/org.dita-community.doctypes && rm
${BRANCH}.zip && \  
#  
# DITA Community Q/A plugin  
#  
wget ${DITA_COMM_URL}org.dita-community.qa/archive/${BRANCH}.zip && unzip
${BRANCH}.zip -d plugins && mv plugins/org.dita-community.qa-${BRANCH}
plugins/org.dita-community.qa && rm ${BRANCH}.zip && \  
#  
# Ruby domain:  
#  
wget ${DITA_COMM_URL}org.dita-community.ruby-d.doctypes/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && mv plugins/org.dita-
community.ruby-d.doctypes-${BRANCH} plugins/org.dita-community.ruby-d.doctypes
&& rm ${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita-community.ruby-d.fo/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && mv plugins/org.dita-
community.ruby-d.fo-${BRANCH} plugins/org.dita-community.ruby-d.fo && rm
${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita-community.ruby-d.html/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && mv plugins/org.dita-
community.ruby-d.html-${BRANCH} plugins/org.dita-community.ruby-d.html && rm
${BRANCH}.zip && \  
#  
# Media domain:  
#  
wget ${DITA_COMM_URL}org.dita-community.media-d.doctypes/archive/${BRANCH}.zip
&& unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && mv plugins/org.dita-
community.media-d.doctypes-${BRANCH} plugins/org.dita-
community.media-d.doctypes && rm ${BRANCH}.zip && \  
wget ${DITA_COMM_URL}org.dita-community.media-d.html/archive/${BRANCH}.zip &&
unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && mv plugins/org.dita-
community.media-d.html-${BRANCH} plugins/org.dita-community.media-d.html && rm
${BRANCH}.zip && \  
#  
# Integrate new plugins  
#  
ant -f integrator.xml  
#  
# End of Dockerfile  
#  
  

