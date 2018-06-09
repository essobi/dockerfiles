FROM ubuntu  
MAINTAINER Sarfaraz Ali Khan <mrkhan1417@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4 xfce4-terminal
tightvncserver  
RUN apt-get install software-properties-common -y  
  
# Themes and icons  
RUN add-apt-repository -y ppa:snwh/pulp; add-apt-repository -y
ppa:tista/adapta  
RUN apt update  
RUN apt-get install paper-icon-theme paper-cursor-theme adapta-gtk-theme -y  
  
  
ENV USER root  
EXPOSE 5901  
  
COPY xsettings.xml /zvnc/xsettings.xml  
COPY xfwm4.xml /zvnc/xfwm4.xml  
  
COPY xstartup /zvnc/xstartup  
  
RUN chmod -R a+rwX /zvnc  
  
COPY start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
CMD ["/opt/start.sh"]  

