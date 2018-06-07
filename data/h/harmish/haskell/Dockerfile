FROM harmish/haskell:tools  
  
# fix for dependency versions  
COPY stack-append.yaml /root/.stack/global-project/stack-append.yaml  
RUN cat /root/.stack/global-project/stack-append.yaml >> /root/.stack/global-
project/stack.yaml && \  
grep -q '^allow-newer:' /root/.stack/config.yaml && \  
sed -i 's/^allow-newer:.*/allow-newer: true/' /root/.stack/config.yaml || \  
printf '\nallow-newer: true' >> /root/.stack/config.yaml && \  
#  
# install diagrams packages and their dependencies  
stack install diagrams diagrams-pgf SVGFonts && \  
apt-get update && \  
apt-get install -y inkscape && \  
#  
# clean-up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

