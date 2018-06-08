FROM java:openjdk-8u66-jdk  
  
RUN groupadd -g 50000 service \  
&& useradd -u 50000 -g service -m service \  
&& curl -fSLs https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "066ad710107dc7ee05d3aa6e4974f01dc98f3888 /bin/tini" | sha1sum -c -  

