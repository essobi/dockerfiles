FROM debian:8  
RUN apt-get -qq update \  
&& apt-get -qq install -y --no-install-recommends sudo wget \  
&& adduser --quiet --shell /bin/bash --gecos "Mprime user,101,," \--disabled-
password mprime \  
&& chown -R mprime:mprime /home/mprime/ \  
&& echo "mprime ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
USER mprime  
WORKDIR /home/mprime  
RUN wget -q http://www.mersenne.org/ftp_root/gimps/p95v2810.linux64.tar.gz -O
./mprime.tar.gz \  
&& tar xzf mprime.tar.gz --absolute-names  
RUN rm -f mprime.tar.gz  
ENTRYPOINT ["./mprime"]  

