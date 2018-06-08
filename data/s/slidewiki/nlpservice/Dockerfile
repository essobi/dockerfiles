FROM openjdk:8-jre  
MAINTAINER Roy Meissner <meissner@informatik.uni-leipzig.de>  
  
WORKDIR /opt/docker  
  
# ---------------- #  
# Installation #  
# ---------------- #  
ADD stage/opt /opt  
RUN echo '\nplay.crypto.secret=${?APPLICATION_SECRET}' >>
conf/application.conf  
  
# ----------------- #  
# Configuration #  
# ----------------- #  
EXPOSE 9000  
# ----------- #  
# Cleanup #  
# ----------- #  
RUN apt-get autoremove -y && apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
# -------- #  
# Run! #  
# -------- #  
ENTRYPOINT []  
CMD ["bin/nlp-services"]  

