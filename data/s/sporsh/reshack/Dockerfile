FROM monokrome/wine  
MAINTAINER Geir Sporsheim <geir.sporsheim@gmail.com>  
  
  
# Install wget  
RUN apt-get install -y wget  
  
# Download and install Resource Hacker  
RUN wget "http://www.angusj.com/resourcehacker/reshack_setup.exe"  
RUN xvfb-run -a wine reshack_setup.exe /sp- /silent /norestart
/dir="Z:\opt\reshack"  
RUN rm reshack_setup.exe  
  
ENTRYPOINT ["xvfb-run", "-a", "wine", "/opt/reshack/ResHacker.exe"]  

