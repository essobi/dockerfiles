FROM buildpack-deps:xenial  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
ca-certificates \  
wget \  
gdebi \  
&& rm -r /var/lib/apt/lists/*  
  
RUN wget https://minergate.com/download/deb-cli  
RUN mv deb-cli deb-cli.deb  
RUN gdebi --non-interactive deb-cli.deb  
RUN rm *.deb  
  
ENTRYPOINT ["minergate-cli"]  
CMD ["-user", "maxim1@email.cz", "-xmr"]

