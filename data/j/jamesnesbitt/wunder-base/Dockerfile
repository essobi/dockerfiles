FROM centos  
MAINTAINER james.nesbitt@wunderkraut.com  
  
### WUNDER BASE --------------------------------------------------------------  
## EPEL Dependency on CentOS 7 and Fedora EPEL 7 #  
RUN /usr/bin/yum \--assumeyes \--verbose install epel-release  
  
# We could consider running real systemd, instead of the fake, but it probably
still can't get dbus running, until kdbus gets into kernel (4.1 probably).  
#RUN /usr/bin/yum remove -y fakesystemd && /usr/bin/yum install -y systemd  
# Update and clean - not really necessary, just use the latest CentOS, and it
will be pretty much up to date  
#RUN /usr/bin/yum update -y && /usr/bin/yum clean -y all  
# Install some tools used here. (openssl is needed only for password
generation below, hostname prevents a number of operations from giving
warnings)  
# Other packages to consider : unzip tar git (git has a lot of perl deps)  
RUN /usr/bin/yum \--assumeyes \--verbose install hostname openssl  
  
# Create the base for our convention of using /app for the application  
ADD app /app  
# Create two users to share UIDs across all systems  
# - core : 500 : this is a user who's uid would match that of a CoreOS host;  
# - app : 1000 : this is the primary application user who will own files, and
who's group will have access to those files (SHOULD WE ALSO? : --root /app ;
seems a little bit overzealous, and might mess over some of the subboxes.)  
# (we generate random password, everytime this image is built. (yes it used
openssl; twice even)  
RUN /sbin/groupadd \--gid 500 core && \  
/usr/sbin/adduser \--home-dir /home/core \--uid 500 \--gid 500 \--shell
/bin/nologin \--password "`openssl rand -base64 32 | openssl passwd -1
-stdin`" \--comment "CoreOS UID User" core  
RUN /sbin/groupadd \--gid 1000 app && \  
/usr/sbin/adduser \--no-create-home \--home-dir /app \--uid 1000 \--gid 1000
\--shell /bin/nologin \--password "`openssl rand -base64 32 | openssl passwd
-1 -stdin`" \--comment "application login" app && \  
chown -R app:app /app  
  
CMD ["/bin/bash"] # Used just to prevent certain types of RemoteAPI failures  
### WUNDER BASE -------------------------------------------------------------  

