FROM node:6.9  
# Install strong-build/strong-pm/strong-deploy  
RUN useradd -ms /bin/bash strong-pm \  
&& chown -R strong-pm:strong-pm /usr/local \  
&& su strong-pm -c "npm install -g strong-build strong-pm strong-deploy && npm
cache clean"

