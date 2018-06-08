FROM gittools/libgit2sharp-mono  
LABEL maintainer="Erik Hvattum <erik.hvattum@gmail.com>"  
  
ADD entrypoint.sh /entrypoint.sh  
ADD gitversion.sh /gitversion.sh  
  
# Install GitVersion 4  
RUN curl -Ls
https://github.com/GitTools/GitVersion/releases/download/v4.0.0-beta.12/GitVersion.CommandLine.4.0.0-beta0012.nupkg
-o tmp.zip \  
&& unzip -d /usr/lib/GitVersion tmp.zip \  
&& rm tmp.zip \  
&& sed -i 's|lib/linux/x86_64|/usr/lib/GitVersion/tools/lib/linux/x86_64|g'
/usr/lib/GitVersion/tools/LibGit2Sharp.dll.config \  
&& chmod +x /entrypoint.sh \  
&& chmod +x /gitversion.sh \  
&& ln -s /gitversion.sh /usr/bin/gitversion  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD ["gitversion"]  

