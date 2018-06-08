FROM ubuntu:trusty  
MAINTAINER Kyle Anderson <kyle@xkyle.com>  
  
RUN apt-get update -y  
RUN apt-get install -y software-properties-common  
RUN /usr/bin/apt-add-repository -y ppa:ubuntu-wine/ppa  
RUN dpkg --add-architecture i386  
RUN apt-get update -y  
  
RUN apt-get install -y wine1.7  
RUN apt-get install -y winetricks xvfb  
RUN apt-get -y install winbind  
  
ENV WINEPREFIX /root/prefix32  
ENV WINEARCH win32  
  
#POWER SHELL 1.0  
RUN xvfb-run winetricks --unattended dotnet20  
RUN wget -O /tmp/WindowsXP-KB926139-v2-x86-ENU.exe
http://download.microsoft.com/download/7/3/4/7345bb7d-0b07-40e8-9480-5b8c55b9c8b7/WindowsXP-
KB926139-v2-x86-ENU.exe  
RUN winetricks --unattended winxp  
RUN apt-get -y install psmisc  
ADD xvfb-wrapper.sh /usr/bin/  
RUN /usr/bin/xvfb-wrapper.sh wine /tmp/WindowsXP-KB926139-v2-x86-ENU.exe
/quiet /passive /norestart  
RUN /usr/bin/test -e
/root/prefix32/drive_c/windows/system32/windowspowershell/v1.0/powershell.exe  
  
ENV WINEDEBUG -all  
# I couldn't get a raw exec to work for some reason  
ADD ps-wrapper.sh /usr/bin/  
CMD [ "/bin/bash", "/usr/bin/ps-wrapper.sh" ]  

