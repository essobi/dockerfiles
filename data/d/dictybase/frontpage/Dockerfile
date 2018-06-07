FROM node:0.10.38  
MAINTAINER David Jimenez-Morales <biodavidjm@gmail.com>  
  
# Install sudo  
RUN apt-get -y update \  
&& apt-get -y install sudo \  
&& rm -rf /var/lib/apt/lists/* \  
# Add an user that will be used for install purpose  
&& useradd -m -r -s /sbin/nologin -c "Docker image user" caboose \  
&& chown -R caboose /home/caboose \  
# Can run passwordless sudo  
&& adduser caboose sudo \  
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Set as default user  
USER caboose  
  
# Clone the source code  
RUN cd /home/caboose/ && git clone \--branch v0.4.9
https://github.com/dictyBase/frontpage-dictybase.git  
  
# Source code folder will be the default landing spot  
WORKDIR /home/caboose/frontpage-dictybase  
  
# Env to include binaries inside node_modules folder  
# Make sure this works  
ENV PATH node_modules/.bin:$PATH  
  
# Install npm dependencies  
# Install bower dependencies  
RUN npm install --production \  
&& bower install  
  
# Startup script  
ADD app.sh /home/caboose/frontpage-dictybase/  
  
# Default command  
# Move the build to the /www folder  
CMD ["/home/caboose/frontpage-dictybase/app.sh"]  
  

