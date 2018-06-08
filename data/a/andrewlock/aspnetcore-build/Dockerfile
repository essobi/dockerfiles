# Build image  
FROM microsoft/aspnetcore-build:2.0.8-2.1.200 AS builder  
WORKDIR /sln  
  
ONBUILD COPY ./*.sln ./NuGet.config ./*.props ./*.targets ./  
  
# Copy the main source project files  
ONBUILD COPY src/*/*.csproj ./  
ONBUILD RUN for file in $(ls *.csproj); do mkdir -p src/${file%.*}/ && mv
$file src/${file%.*}/; done  
# Copy the test project files  
ONBUILD COPY test/*/*.csproj ./  
ONBUILD RUN for file in $(ls *.csproj); do mkdir -p test/${file%.*}/ && mv
$file test/${file%.*}/; done  
  
ONBUILD RUN dotnet restore  
  
ONBUILD COPY ./test ./test  
ONBUILD COPY ./src ./src  
  
# This defines the `ARG` inside the build-stage (it will be executed after
`FROM`  
# in the child image, so it's a new build-stage). Don't set a default value so
that  
# the value is set to what's currently set for `BUILD_VERSION`  
ONBUILD ARG BUILD_VERSION  
  
# If BUILD_VERSION is set/non-empty, use it, otherwise use a default value  
ONBUILD ARG VERSION=${BUILD_VERSION:-1.0.0}  
  
ONBUILD RUN dotnet build /p:Version=$VERSION -c Release --no-restore  
  
ONBUILD RUN find ./test -name '*.csproj' -print0 | xargs -L1 -0 dotnet test
/p:Version=$VERSION -c Release --no-build --no-restore

