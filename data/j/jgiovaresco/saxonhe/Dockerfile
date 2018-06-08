#  
# docker run -it --rm=true \  
# -e USER=$USER -e USERID=$UID \  
# /mydata:/data \  
# --name saxonhe jgiovaresco/saxonhe \  
# -ext:off -s:myfile.xml -xsl:mysheet.xsl -o:myoutput  
FROM debian:jessie  
MAINTAINER Julien Giovaresco <dev@giovaresco.fr>  
  
RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libsaxonhe-java \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd saxonhe \  
&& mkdir /data \  
&& chown saxonhe:saxonhe /data  
  
USER saxonhe  
WORKDIR /data  
  
ENTRYPOINT ["java", "-jar", "/usr/share/java/Saxon-HE.jar"]  
CMD [""]

