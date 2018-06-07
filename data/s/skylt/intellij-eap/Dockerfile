FROM alekzonder/archlinux-yaourt:latest  
  
MAINTAINER Brendan Harley <brendan@lse.epita.fr>  
  
USER root  
  
ENV _JAVA_AWT_WM_NONREPARENTING=1  
  
RUN sudo -u yaourt yaourt --noconfirm -S intellij-idea-ue-eap  
  
RUN sudo -u yaourt yaourt --noconfirm -S gradle  
  
RUN sudo -u yaourt yaourt --noconfirm -S libxrender  
  
RUN sudo -u yaourt yaourt --noconfirm -S jdk9-openjdk  
  
ENTRYPOINT ["/usr/bin/idea-ue-eap"]  
  
USER 1000  

