FROM gentoo/stage3-amd64:latest  
MAINTAINER Lara Maia - dev@lara.click  
LABEL Description="Gentoo with portage, git, repoman, systemd"  
  
ADD install_portage.sh /  
ADD set_config.sh /  
ADD update_system.sh /  
ADD install_extra_packages.sh /  
  
RUN /install_portage.sh  
RUN /set_config.sh  
RUN /update_system.sh  
RUN /install_extra_packages.sh  

