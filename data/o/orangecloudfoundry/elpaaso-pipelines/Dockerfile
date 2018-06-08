FROM orangecloudfoundry/elpaaso-pipelines:base  
  
RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary" -o
cf.tgz \  
&& tar -xvf cf.tgz \  
&& chmod +x cf \  
&& mv cf /usr/bin  
  
RUN curl -L
"https://github.com/concourse/autopilot/releases/download/0.0.2/autopilot-
linux" -o autopilot \  
&& chmod +x autopilot \  
&& cf install-plugin ./autopilot -f  
RUN curl -L
"https://github.com/odlp/antifreeze/releases/download/v0.3.0/antifreeze-linux"
-o antifreeze \  
&& chmod +x antifreeze \  
&& cf install-plugin ./antifreeze -f  

