FROM node:5.9  
MAINTAINER "Sascha Marcel Schmidt" <docker@saschaschmidt.net>  
  
RUN apt-get update && apt-get install ruby locales -y --no-install-recommends
&& rm -r /var/lib/apt/lists/*  
# Configure timezone and locale  
RUN echo "Europe/Berlin" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_GB.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_GB.UTF-8  
ENV LANG="en_GB.UTF-8"  
ENV LANGUAGE="en_GB.UTF-8"  
ENV LC_ALL="en_GB.UTF-8"  
RUN gem install sass  
RUN useradd -m node  
WORKDIR /home/node/  
COPY vendor /home/node/vendor  
RUN mkdir config  
COPY package.json /home/node/  
RUN chown node.node -R /home/node/  
USER node  
RUN echo "{}" >> bower.json  
COPY .bowerrc /home/node/.bowerrc  
RUN npm install  
  
COPY Gruntfile.js /home/node/  
VOLUME ["/home/node/config"]  
CMD ["/home/node/node_modules/grunt-cli/bin/grunt"]  

