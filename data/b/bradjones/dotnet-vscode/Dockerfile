FROM bradjones/dotnet-ide:latest  
LABEL maintainer "brad@bjc.id.au"  
# Install the vscode repo  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg && \  
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \  
echo "deb [arch=amd64] http://packages.microsoft.com/repos/vscode stable main"
> /etc/apt/sources.list.d/vscode.list  
  
# Install vscode it's self  
RUN apt-get update && apt-get install -y --no-install-recommends code && apt-
get clean && rm -rf /var/lib/apt/lists/*

