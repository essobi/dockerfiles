FROM openjdk:8  
  
RUN curl -L
'https://cli.run.pivotal.io/stable?release=debian64&version=6.29.0&source=github-
rel' -o cf-cli.deb \  
&& dpkg -i cf-cli.deb \  
&& rm -f cf-cli.deb  

