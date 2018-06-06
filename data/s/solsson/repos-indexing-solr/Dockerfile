FROM
solr:6.4@sha256:2d74cd53ce4d43be58d4074302f4b7f1d75b7a73b07ef6034bebd2e5f2986245  
  
ENV reposIndexingVersion=1754fd9b2728fd9c4577b19b03f709bed262a038  
ENV xmlIndexingVersion=bc0c2282894bf36dbad609fdaa0534ae3ba298c5  
  
RUN cd server/solr \  
&& curl -SL https://github.com/Reposoft/repos-
indexing/archive/$reposIndexingVersion.tar.gz -o repos-indexing.tar.gz \  
&& tar xvzf repos-indexing.tar.gz --strip-components=8 repos-
indexing-$reposIndexingVersion/src/main/resources/se/repos/indexing/solr/repositem
\  
&& rm repos-indexing.tar.gz  
  
RUN cd server/solr \  
&& curl -SL https://github.com/Simonsoft/cms-indexing-
xml/archive/$xmlIndexingVersion.tar.gz -o cms-indexing-xml.tar.gz \  
&& tar xvzf cms-indexing-xml.tar.gz --strip-components=10 cms-indexing-
xml-$xmlIndexingVersion/src/main/resources/se/simonsoft/cms/indexing/xml/solr/reposxml
\  
&& rm cms-indexing-xml.tar.gz  
  
ADD repositem server/solr/repositem  
ADD reposxml server/solr/reposxml  
  
USER root  
RUN mkdir /solrdata && chgrp $SOLR_USER /solrdata && chmod g+w /solrdata  
USER $SOLR_USER  
VOLUME /solrdata

