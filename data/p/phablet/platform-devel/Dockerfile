FROM phablet/platform-devel-base:trusty-openjdk-7  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
bc \  
genisoimage \  
lib32ncurses5-dev \  
lib32ncursesw5-dev \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  

