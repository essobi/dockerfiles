FROM opensuse:leap  
  
MAINTAINER Mauro Morales "mamorales@suse.com"  
RUN zypper -n --gpg-auto-import-keys refresh  
RUN zypper -n --gpg-auto-import-keys update  
RUN zypper ar -G -f
http://download.opensuse.org/repositories/systemsmanagement:/machinery/openSUSE_Leap_42.1/
machinery  
RUN zypper -n --gpg-auto-import-keys install openssh less machinery  

