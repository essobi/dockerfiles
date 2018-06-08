# comment to force rebuild, aw yeah!  
FROM overview/overview-base  
  
EXPOSE 9000  
RUN \  
export FILENAMES="$(unzip -qq -p production.zip archive/web/classpath.txt | \  
sed -e 's/^/archive\/lib\//')" && \  
unzip -qq -d bin -j production.zip $FILENAMES && \  
rm production.zip  
  
WORKDIR /opt/overview  
  
CMD ["/usr/bin/java", \  
"-cp", "bin/*", \  
"-Dfile.encoding=UTF8", \  
"-Duser.timezone=UTC", \  
"-Dpidfile.path=/dev/null", \  
"play.core.server.ProdServerStart"]  

