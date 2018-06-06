FROM maven  
  
#Needed to add key for cf-cli  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends apt-transport-https  
  
#Install cf-cli  
#https://docs.cloudfoundry.org/cf-cli/install-go-cli.html  
RUN wget -q -O -
https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key
add -  
RUN echo "deb http://packages.cloudfoundry.org/debian stable main" | tee
/etc/apt/sources.list.d/cloudfoundry-cli.list  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends cf-cli  
RUN cf add-plugin-repo CF-Community https://plugins.cloudfoundry.org  
RUN cf install-plugin blue-green-deploy -r CF-Community -f  
  
# Install Chromium  
#RUN apt-get update && apt-get install -y curl xvfb chromium  
RUN apt-get install -y libxss1  
#ADD xvfb-chromium /usr/bin/xvfb-chromium  
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome  
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser

