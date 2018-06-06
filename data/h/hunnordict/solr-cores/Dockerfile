FROM solr:7.3.1  
RUN echo "SOLR_OPTS=\"\$SOLR_OPTS -Dsolr.allow.unsafe.resourceloading=true\""
>> bin/solr.in.sh  
RUN echo "SOLR_OPTS=\"\$SOLR_OPTS -Dlucene.match.version=7.3.1\"" >>
bin/solr.in.sh  
  
ENV HUNNOR_DUMP_FILE_HU hunnor-hu.xml  
ENV HUNNOR_DUMP_FILE_NB hunnor-nb.xml  
  
RUN echo "SOLR_OPTS=\"\$SOLR_OPTS -Dhunnor.dump.dir.hu=\$(dirname
/hunnor/\$HUNNOR_DUMP_FILE_HU)\"" >> bin/solr.in.sh  
RUN echo "SOLR_OPTS=\"\$SOLR_OPTS -Dhunnor.dump.file.hu=\$(basename
/hunnor/\$HUNNOR_DUMP_FILE_HU)\"" >> bin/solr.in.sh  
RUN echo "SOLR_OPTS=\"\$SOLR_OPTS -Dhunnor.dump.dir.nb=\$(dirname
/hunnor/\$HUNNOR_DUMP_FILE_NB)\"" >> bin/solr.in.sh  
RUN echo "SOLR_OPTS=\"\$SOLR_OPTS -Dhunnor.dump.file.nb=\$(basename
/hunnor/\$HUNNOR_DUMP_FILE_NB)\"" >> bin/solr.in.sh  
  
RUN echo "SOLR_HEAP=1024m" >> bin/solr.in.sh  
  
RUN rm -r /opt/solr/server/solr/*  
  
COPY field-types.xml server/solr  
COPY hunnor.hu server/solr/hunnor.hu  
COPY hunnor.nb server/solr/hunnor.nb  
COPY lib server/solr/lib  
COPY solr.xml server/solr  
  
USER root  
  
RUN chown -R $SOLR_USER:$SOLR_USER server/solr  
  
RUN mkdir -p /var/opt/solr/data/  
RUN chown -R $SOLR_USER:$SOLR_USER /var/opt/solr/data/  
  
USER $SOLR_USER  

