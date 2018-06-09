FROM prolucid/storm-base:0.0.3  
MAINTAINER Daniel Covello  
  
# The versions (github branches) that should be pulled and compiled  
ENV MONO_VERSION=4.2.3.4  
ENV FS_VERSION=4.0.0.3-0xamarin1  
  
# Install F# + Mono  
ENV SETUP_TOOLS="make pkg-config git autoconf libtool automake build-essential
gettext "  
WORKDIR /deploy  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/$MONO_VERSION main" | tee /etc/apt/sources.list.d/mono-
xamarin.list && \  
apt-get update && \  
apt-get install -y mono-complete fsharp=$FS_VERSION  
  
# Configure supervisor startup script  
RUN sed -i -e "s/%STORMAPP%/supervisor/g" /etc/service/storm/run  
RUN chmod +x /etc/service/storm/run  
  
EXPOSE 6700 6701 6702 6703 8000  

