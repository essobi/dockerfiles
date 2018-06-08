  
FROM java:8  
MAINTAINER Rafael Pax <rpax@ucm.es>  
  
ENV BLENDER_MAJOR 2.76  
ENV BLENDER_VERSION 2.76b  
ENV BLENDER_BZ2_URL
http://mirror.cs.umn.edu/blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-
linux-glibc211-x86_64.tar.bz2  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install unzip zip curl bzip2 libfreetype6 maven  
  
RUN mkdir /usr/local/blender  
RUN curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2  
RUN tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1  
RUN rm blender.tar.bz2  
  
#
------------------------------------------------------------------------------  
# disable interactive functions  
ENV ADDONS_FOLDER /usr/local/blender/$BLENDER_MAJOR/scripts/addons  
  
  
  
# Addons & Tools  
RUN mkdir -p "$ADDONS_FOLDER"  
RUN curl --remote-name https://bitbucket.org/rpax/mhx2-makehuman-
exchange/get/tip.zip  
RUN unzip tip.zip  
RUN rm tip.zip  
RUN mv rpax-mhx2-makehuman-exchange-5971f82e50f3/import_runtime_mhx2
"$ADDONS_FOLDER/import_runtime_mhx2"  
RUN rm -rf rpax-mhx2-makehuman-exchange-5971f82e50f3  
  
# makehuman blender tools  
RUN curl --remote-name
http://download.tuxfamily.org/makehuman/releases/1.1.0/blendertools-1.1.0-all.zip  
RUN unzip blendertools-1.1.0-all.zip  
RUN rm blendertools-1.1.0-all.zip  
RUN mv blendertools/makeclothes "$ADDONS_FOLDER/makeclothes"  
RUN mv blendertools/maketarget "$ADDONS_FOLDER/maketarget"  
RUN mv blendertools/makewalk "$ADDONS_FOLDER/makewalk"  
RUN rm -rf blendertools  
  
# Maven copy & build  
COPY massis-makehuman ~/massis-makehuman  
WORKDIR ~/massis-makehuman  
  
# force download of everything  
RUN mvn clean install exec:java
-Dexec.mainClass="com.massisframework.makehuman.BlenderConverter"  
  
COPY docker-files/scripts/mixamo_to_blender.py /usr/bin/mixamo_to_blender.py  
RUN chmod +x /usr/bin/mixamo_to_blender.py  
  
#COPY docker-files/animations /animations  
COPY docker-files/scripts/run-converter.sh /bin/run-converter  
RUN chmod 777 /bin/run-converter  
  
VOLUME /animations  
VOLUME /input  
VOLUME /output  
  
ENTRYPOINT ["/bin/bash"]  

