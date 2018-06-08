FROM microsoft/dotnet:1.1.2-sdk  
  
WORKDIR /usr/src/  
  
# Install dependencies for layer cache  
COPY ./MoEmbed.sln ./MoEmbed.sln  
COPY ./MoEmbed.App/MoEmbed.App.csproj ./MoEmbed.App/MoEmbed.App.csproj  
COPY ./MoEmbed.Models/MoEmbed.Models.csproj
./MoEmbed.Models/MoEmbed.Models.csproj  
COPY ./MoEmbed.Models.Tests/MoEmbed.Models.Tests.csproj
./MoEmbed.Models.Tests/MoEmbed.Models.Tests.csproj  
COPY ./MoEmbed.Core/MoEmbed.Core.csproj ./MoEmbed.Core/MoEmbed.Core.csproj  
COPY ./MoEmbed.Core.Tests/MoEmbed.Core.Tests.csproj
./MoEmbed.Tests/MoEmbed.Core.Tests.csproj  
COPY ./MoEmbed.Twitter/MoEmbed.Twitter.csproj
./MoEmbed.Twitter/MoEmbed.Twitter.csproj  
COPY ./MoEmbed.Twitter.Tests/MoEmbed.Twitter.Tests.csproj
./MoEmbed.Tests/MoEmbed.Twitter.Tests.csproj  
RUN dotnet restore  
  
# Copy entire source code  
COPY ./MoEmbed.App ./MoEmbed.App  
COPY ./MoEmbed.Models ./MoEmbed.Models  
COPY ./MoEmbed.Models.Tests ./MoEmbed.Models.Tests  
COPY ./MoEmbed.Core ./MoEmbed.Core  
COPY ./MoEmbed.Core.Tests ./MoEmbed.Core.Tests  
COPY ./MoEmbed.Twitter ./MoEmbed.Twitter  
COPY ./MoEmbed.Twitter.Tests ./MoEmbed.Twitter.Tests  
  
# Build app  
WORKDIR /usr/src/MoEmbed.App  
RUN dotnet restore  
RUN dotnet publish -c Release -o out  
  
FROM microsoft/dotnet:1.1.2-runtime  
WORKDIR /usr/app  
COPY \--from=0 /usr/src/MoEmbed.App/out/ .  
CMD dotnet ./MoEmbed.App.dll  

