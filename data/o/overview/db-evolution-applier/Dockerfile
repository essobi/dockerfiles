FROM overview/overview-base  
  
RUN \  
export FILENAMES="$(unzip -qq -p production.zip archive/db-evolution-
applier/classpath.txt | \  
sed -e 's/^/archive\/lib\//')" && \  
unzip -qq -d bin -j production.zip $FILENAMES && \  
rm production.zip  
  
WORKDIR /opt/overview  
  
CMD ["/usr/bin/java", \  
"-cp", "bin/*", \  
"-Dfile.encoding=UTF8", \  
"-Duser.timezone=UTC", \  
"com.overviewdocs.db_evolution_applier.Main"]  
  

