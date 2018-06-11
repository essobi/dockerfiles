FROM phusion/baseimage:0.10.0  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
#------------------------------------------------------------------------------  
## Install dependencies  
RUN apt-get update \  
&& apt-get -y install \  
aria2 \  
unzip  
  
## Create a urt user  
RUN useradd \--home-dir /home/urt \--create-home urt  
  
## Download Urban Terror  
## if links are broken, check http://www.urbanterror.info/downloads/  
ARG CHECKSUM_UrbanTerror433_full_zip=0eaafc4dce579310e3061050f6bbd7a9  
RUN aria2c \--file-allocation=none \  
\--checksum=md5=$CHECKSUM_UrbanTerror433_full_zip \  
\--check-integrity \  
http://cdn.urbanterror.info/urt/43/releases/zips/UrbanTerror433_full.zip \  
https://up.barbatos.fr/urt/UrbanTerror433_full.zip \  
https://www.happyurtday.com/releases/4x/UrbanTerror433_full.zip \  
\--dir=/tmp \  
&& unzip /tmp/UrbanTerror43*.zip -d /home/urt && rm /tmp/UrbanTerror43*.zip \  
&& chown -R urt:urt /home/urt/ \  
&& chmod +x /home/urt/UrbanTerror43/Quake3-UrT-Ded.*  

