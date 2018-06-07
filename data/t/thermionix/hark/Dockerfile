from ubuntu:12.10  
env DEBIAN_FRONTEND noninteractive  
  
run apt-get install -y --no-install-recommends software-properties-common  
  
run apt-add-repository -y ppa:chris-lea/node.js && apt-get update  
  
run apt-get install -q -y git nodejs build-essential python  
  
run git clone https://github.com/joelhans/Hark.git /usr/share/hark  
  
run cd /usr/share/hark ; npm install  
  
#volume /usr/share/hark  
expose 3000  
cmd node /usr/share/hark/app.js  

