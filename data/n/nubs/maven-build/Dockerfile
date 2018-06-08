FROM base/archlinux:latest  
  
MAINTAINER Spencer Rinehart <anubis@overthemonkey.com>  
  
# Update system and install java/maven.  
RUN pacman --sync --refresh --sysupgrade --noconfirm --noprogressbar --quiet
&& pacman --sync --noconfirm --noprogressbar --quiet jdk7-openjdk maven  
  
# Create a separate user to run mvn as. Root access shouldn't typically be  
# necessary. Specify the uid so that it is unique including from the host.  
RUN useradd --uid 51177 --create-home --comment "Build User" build  
  
RUN mkdir /code && chown build:build /code  
WORKDIR /code  
  
USER build  
ENV HOME /home/build  
  
# Set the umask to 002 so that the group has write access inside and outside
the  
# container.  
ADD umask.sh $HOME/umask.sh  
  
ENTRYPOINT ["/home/build/umask.sh"]  
CMD ["mvn"]  

