from node:latest  
maintainer Efthymios Sarmpanis <e.sarbanis@gmail.com>  
  
# Install Chrome  
run wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
run sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
run apt-get update -y  
run apt-get install google-chrome-stable -y  
  
# Install Firefox  
run sh -c 'echo "deb http://packages.linuxmint.com debian import" >>
/etc/apt/sources.list.d/mint.list'  
run apt-get update -y  
run apt-get install firefox --force-yes -y  
  
cmd ["node"]  

