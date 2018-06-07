FROM ubuntu:18.04  
  
# allows the software-properties-common package to be found, which is  
# needed to add the ppa  
RUN apt-get update -y  
RUN apt-get install -y software-properties-common  
  
# installs sudo and XAuth, which are needed for the process that  
# accesses the host's XServer  
# Xauthority needs to be installed in the image, as the run script  
# - run_gscan.sh -will dynamically create an Xauthority file on the  
# host machine and pass it to the container at runtime  
RUN apt-get install -y sudo  
RUN apt-get install -y xauth  
  
# adds the jeffreyratcliffe ppa that contains the gscan2pdf software  
RUN add-apt-repository ppa:jeffreyratcliffe/ppa  
  
# update the newly-added ppa  
RUN apt-get update -y  
  
# the app will run without these packages, but you will get errors;  
# the gnome-icon-theme package is used for the icons in the app  
RUN apt-get install -y packagekit-gtk3-module  
RUN apt-get install -y libcanberra-gtk*  
RUN apt-get install -y gnome-icon-theme  
  
# Install the scanner software  
RUN apt-get install -y gscan2pdf  
  
# the app looks for a default pdf viewer - I find this preferable  
# to a browser, since it has far more options for editing  
# autolaunch can be enabled/disabled with the "post-save hooks"  
# option that appears when saving  
RUN apt-get install -y gimp  
  
# Runs a script that creates a copy of the host user's account  
# in the container thus allowing access to the host XServer via  
# the Xauthority file passed into the container.  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  
# Clean up after the install and update processes  
RUN apt-get autoremove &&\  
apt-get clean &&\  
rm -rf /tmp/*  
  
  
  

