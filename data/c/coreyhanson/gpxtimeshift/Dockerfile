FROM node:9 as download  
LABEL maintainer "Corey Ryan Hanson"  
  
#Installs git and downloads from repository.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
--no-install-recommends -y \  
git \  
ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/kssfilo/gpxtimeshift.git && \  
cd gpxtimeshift && \  
git checkout c7e0020b20ed839951c8ccd82f9e03304dfd1d55  
  
#Starts new image copying over the source code from phase 1.  
FROM node:9  
COPY \--from=download /gpxtimeshift /gpxtimeshift  
  
RUN cd gpxtimeshift && \  
npm install -g gpxtimeshift && \  
userdel -r node  
  
#Creates unprivileged user.  
COPY /create-user.sh /  
RUN chmod +x create-user.sh  
ARG docker_root_pass=flytouchthesun  
ARG docker_unprivileged_user=strava  
ARG docker_unprivileged_pass=icarus  
RUN /create-user.sh && \  
rm /create-user.sh  
  
#Copies the shell script that runs the program.  
COPY gpx-init.sh /user/local/bin/sh/  
RUN chmod +x /user/local/bin/sh/gpx-init.sh && \  
sed -i "s/\$docker_unprivileged_user/$docker_unprivileged_user/g"
/user/local/bin/sh/gpx-init.sh  
  
#Switches to unprivileged user.  
USER $docker_unprivileged_user  
WORKDIR /home/$docker_unprivileged_user  
  
CMD /user/local/bin/sh/gpx-init.sh  

