## Dockerfile for Isabelle2017  
FROM debian:stretch-slim  
SHELL ["/bin/bash", "-c"]  
  
ENV VERSION 2017  
# packages  
RUN apt-get -y update && \  
apt-get install -y curl less lib32stdc++6 libgomp1 libwww-perl rlwrap unzip
wget texlive texlive-latex-extra texlive-math-extra && \  
apt-get clean  
  
# user  
RUN useradd -m isabelle && (echo isabelle:isabelle | chpasswd)  
USER isabelle  
  
# Isabelle  
WORKDIR /home/isabelle  
RUN wget -q -O Isabelle.tar.gz
http://isabelle.in.tum.de/dist/Isabelle${VERSION}_app.tar.gz  
RUN tar xzf Isabelle.tar.gz && \  
mv Isabelle${VERSION} Isabelle && \  
rm -rf Isabelle.tar.gz Isabelle/contrib/jdk/x86-linux && \  
perl -pi -e
's,ISABELLE_HOME_USER=.*,ISABELLE_HOME_USER="\$USER_HOME/.isabelle",g;'
Isabelle/etc/settings && \  
perl -pi -e 's,ISABELLE_LOGIC=.*,ISABELLE_LOGIC=HOL,g;' Isabelle/etc/settings
&& \  
Isabelle/bin/isabelle build -s -b HOL HOL-Library HOL-Computational_Algebra
HOL-Algebra  
  
ENTRYPOINT ["Isabelle/bin/isabelle"]  

