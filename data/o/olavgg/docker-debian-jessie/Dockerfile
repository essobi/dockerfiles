# VERSION 0.3  
# AUTHOR: Olav Grønås Gjerde <olav@backupbay.com>  
# DESCRIPTION: Image based on Debian Jessie with extra tools  
# TO_BUILD: docker build -t my_custom_jessie .  
FROM debian:jessie  
MAINTAINER olav@backupbay.com  
  
# Update the repository indexes  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y procps vim-tiny bash dialog  
  
# Add warning message if someone tries to exit container  
RUN echo "alias exit='if [ \"\$(id -un)\" == \"root\" ];then dialog "\  
"--title \"Warning\" --defaultno "\  
"--yesno \"Exit will shut down the container. "\  
"Really exit?\" 5 55;[ \$? == 0 ] && exit;else exit; fi;'" >> /etc/profile  

