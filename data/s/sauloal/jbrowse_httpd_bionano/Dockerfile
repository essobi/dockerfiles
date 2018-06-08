FROM sauloal/jbrowse_httpd  
  
RUN git clone https://github.com/bionanogenomics/JBrowsePlugin.git
/jbrowse/plugins/BioNanoGenomics && \  
echo '{"plugins":["BioNanoGenomics"]}' > /jbrowse/jbrowse_conf.json  
  

