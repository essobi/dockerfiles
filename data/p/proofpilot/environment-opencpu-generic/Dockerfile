FROM proofpilot/environment-opencpu-generic:generic  
MAINTAINER Volodymyr Sheptytsky <vshept@hotmail.com>  
  
ENV GIT_TOKEN="5bfae573af3eb9eff8cb52c1beb2be2580b6fcb3"  
ENV SOME_C="ServerName opencpu.proofpilot.com"  
  
  
  
#########################################################################################  
# Installing project  
#########################################################################################  
  
  
RUN echo "004"  
  
# Get code from repo  
RUN mkdir /tmp/OpenCPU \  
&& curl -H "Authorization: token $GIT_TOKEN" \  
-L https://api.github.com/repos/ProofPilot/OpenCPU/tarball/master | \  
tar -xz --strip 1 -C /tmp/OpenCPU \  
&& ls -l /tmp  
RUN rm -rf /home/rstudio/r-ppv3 || true \  
&& mv -f /tmp/OpenCPU/r-ppv3 /home/rstudio/ \  
&& rm -rf /tmp/OpenCPU \  
&& chown -R rstudio:rstudio /home/rstudio/r-ppv3 \  
&& find /home/rstudio/ -type d | xargs chmod a+x \  
&& chmod -R a+rw /home/rstudio  
  
COPY etc/ /etc/  
  
WORKDIR /home/rstudio/r-ppv3  
RUN R CMD build `ls -d */`  
RUN R CMD INSTALL *.tar.gz  
  
RUN chown -R rstudio:rstudio /home/rstudio/r-ppv3 \  
&& find /home/rstudio/ -type d | xargs chmod a+x \  
&& chmod -R a+rw /home/rstudio  
##########################################################################################  
  
  
EXPOSE 80

