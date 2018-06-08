FROM rickdesantis/ubuntu-lxde  
MAINTAINER Riccardo B. Desantis <riccardobenito.desantis@gmail.com>  
  
# Setting the environment  
ENV HOSTNAME firefox.rickdesantis.docker.com  
  
# Update the repos and install all the used packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
firefox && \  
rm -rf /var/lib/apt/lists/*  
  
# Create a link to firefox on the desktop and put it in autostart  
WORKDIR ${USERHOME}  
RUN cp /usr/share/applications/firefox.desktop Desktop/ && \  
sed 's|%u||' </usr/share/applications/firefox.desktop
>.config/autostart/firefox.desktop  
  
# Build: docker build -t firefox1 ../firefox  
# Run: docker run --name=firefox1 -p 5901:5901 -p 3389:3389 firefox1 &  
# Bash: docker exec -it firefox1 bash  
# Start: docker start firefox1  
# Stop: docker stop firefox1  

