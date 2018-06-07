## Dockerfile for Isabelle2017 with HOLCF  
## for internal CI usage  
## based on makarius/isabelle  
FROM debian:latest  
SHELL ["/bin/bash", "-c"]  
  
# packages  
RUN apt-get update && apt-get install -y \  
curl \  
less \  
lib32stdc++6 \  
libgomp1 \  
libwww-perl \  
rlwrap \  
unzip \  
bsdtar \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# user  
RUN useradd -m isabelle && (echo isabelle:isabelle | chpasswd)  
USER isabelle  
  
  
# install Isabelle  
WORKDIR /home/isabelle  
RUN curl --fail --silent
http://isabelle.in.tum.de/dist/Isabelle2017_app.tar.gz > Isabelle.tar.gz  
RUN bsdtar xzf Isabelle.tar.gz && \  
mv Isabelle2017 Isabelle && \  
rm -rf Isabelle.tar.gz Isabelle/contrib/jdk/x86-linux && \  
perl -pi -e
's,ISABELLE_HOME_USER=.*,ISABELLE_HOME_USER="\$USER_HOME/.isabelle",g;'
Isabelle/etc/settings  
  
# set up the logic  
RUN perl -pi -e 's,ISABELLE_LOGIC=.*,ISABELLE_LOGIC=HOLCF,g;'
Isabelle/etc/settings && \  
Isabelle/bin/isabelle build -s -b -j 4 -v HOLCF  
  
ENV PATH="/home/isabelle/Isabelle/bin:${PATH}"  

