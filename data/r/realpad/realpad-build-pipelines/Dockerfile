FROM frekele/gradle:4-jdk8  
  
# Install required packages  
RUN apt-get update \  
&& apt-get install -y git file locales heirloom-mailx \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add script to send static code analyzers reports  
ADD send_reports.sh /send_reports.sh  
RUN chmod +x /send_reports.sh  
  
# Make the "en_US.UTF-8" locale  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  

