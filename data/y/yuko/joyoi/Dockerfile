FROM yuko/joyoi-base  
  
WORKDIR /workdir  
  
# copy helper scripts and actor files  
COPY ./runner /usr/bin  
COPY ./javac-jar.sh /usr/bin/javac-jar  
COPY ./run-actor.sh /actor/  
COPY ./actor.csproj /actor/  
COPY ./Program.cs /actor/  
  
# set file premissions  
RUN chmod +x /usr/bin/runner  
RUN chmod +x /usr/bin/javac-jar  
RUN chmod +x /actor/run-actor.sh  
RUN chmod 755 -R /actor  
RUN chmod 777 -R /workdir  
  
# add user 'runner'  
RUN useradd -m runner  
RUN echo "runner hard nice 19" >> /etc/security/limits.conf  
RUN echo "runner hard nproc 256" >> /etc/security/limits.conf  
RUN echo "root:$(cat /dev/urandom | head -c 30 | base64)" | chpasswd  
  
# restore and build empty actor  
RUN cd /actor && dotnet restore && dotnet build && cd ..  
  
# warming up c#, f#, vb project in user 'runner'  
RUN rm -rf /workdir/*  
RUN su runner -c "cd /workdir && dotnet new console -lang C# && dotnet run"  
RUN rm -rf /workdir/*  
RUN su runner -c "cd /workdir && dotnet new console -lang F# && dotnet run"  
RUN rm -rf /workdir/*  
RUN su runner -c "cd /workdir && dotnet new console -lang VB && dotnet run"  
RUN rm -rf /workdir/*  
  
# trust let's encrypt ca  
# see: https://github.com/certbot/certbot/issues/2026  
COPY ./lets-encrypt-x3-cross-signed.pem /usr/local/share/ca-
certificates/letsencrypt.crt  
RUN update-ca-certificates  

