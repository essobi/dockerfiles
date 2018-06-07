FROM neo4j:2.3  
MAINTAINER pkremer@spurious.biz  
  
# See also https://github.com/jexp/neo4j-shell-tools/tree/2.3  
RUN curl -L https://github.com/infothrill/neo4j-shell-
tools/releases/download/v2.3.3.2/neo4j-shell-tools_2.3.3.zip -o neo4j-shell-
tools.zip && \  
unzip -o neo4j-shell-tools.zip -d lib && \  
rm neo4j-shell-tools.zip  
  
COPY initneo4j.sh /initneo4j.sh  
  
ENTRYPOINT ["/initneo4j.sh"]  
CMD ["neo4j"]  

