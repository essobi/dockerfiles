FROM kelecorix/stack-build:latest  
MAINTAINER sigrlami <sergey.bushnyak@sigrlami.eu>  
  
# Let docker recognize your key  
RUN echo " IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config  
  
# Copy everything to docker ecosystem  
RUN mkdir /code  
WORKDIR /code/  
COPY ./ ./  
  
RUN stack setup --no-docker --upgrade-cabal  
RUN for p in `stack exec \-- ghc-pkg check --simple-output`; do `stack exec
\-- ghc-pkg unregister $p \--force`; done  
RUN stack build --no-docker --verbose  
RUN for p in `stack exec \-- ghc-pkg check --simple-output`; do `stack exec
\-- ghc-pkg unregister $p \--force`; done  
RUN stack install --no-docker  
  
#Copy in necessary content folders  
RUN mkdir /app \  
&& cp ~/.local/bin/plydis /app/ \  
&& cp ~/.local/bin/plydis /code/ \  
&& cp -r /code/snaplets /app/ \  
&& cp -r /code/static /app/ \  
&& cp -r /code/log /app/  
  
COPY docker-entrypoint.sh /  
COPY docker-entrypoint.sh /app  
  
RUN chmod 775 /docker-entrypoint.sh  
RUN chmod 775 /app/docker-entrypoint.sh  
  
#Cleanup  
#RUN apt-get remove stack -y \  
# && apt-get autoclean -y \  
# && apt-get autoremove -y \  
# && rm -rf /var/lib/apt/lists/* \  
# && rm -rf /root/.stack \  
# && rm -rf /code/  
#WORKDIR /app/  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
  
CMD run  

