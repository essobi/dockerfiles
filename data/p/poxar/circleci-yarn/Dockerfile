FROM circleci/node:8  
  
RUN sudo apt-get install -y apt-transport-https  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg \  
| sudo apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" \  
| sudo tee /etc/apt/sources.list.d/yarn.list \  
&& sudo apt-get update \  
&& sudo apt-get install -y yarn  
  
RUN cd /tmp \  
&& wget -q "https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb" \  
&& sudo dpkg -i "google-chrome-stable_current_amd64.deb" \  
|| sudo apt-get install -f \  
&& rm -f "google-chrome-stable_current_amd64.deb"  

