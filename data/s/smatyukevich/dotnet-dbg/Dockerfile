FROM microsoft/aspnetcore  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y unzip
procps  
  
RUN curl -sSL https://aka.ms/getvsdbgsh | bash /dev/stdin -v vs2017u1 -l
~/vsdbg  

