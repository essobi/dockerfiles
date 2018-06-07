FROM jess/chrome  
MAINTAINER Yusuke Watase <ywatase@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
-t testing \  
\--no-install-recommends \  
task-japanese \  
fonts-ipafont \  
fonts-ipafont-gothic \  
fonts-ipafont-mincho \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  

