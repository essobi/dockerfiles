# Build image  
FROM microsoft/aspnetcore-build:2.0.7-2.1.105 AS builder  
WORKDIR /sln  
  
# Install Cake, and compile the Cake builder script  
ENV CAKE_VERSION 0.26.1  
ENV CAKE_TARGET_FRAMEWORK netcoreapp2.0  
COPY ./build.sh ./build.cake ./  
RUN ./build.sh build.cake --target=Clean  
  
# Copy the actual app and allow overriding the cake build script  
ONBUILD COPY ./*.sln ./NuGet.config ./*.props ./*.targets ./  
  
# Copy the main source project files  
ONBUILD COPY src/*/*.csproj ./  
ONBUILD RUN for file in $(ls *.csproj); do mkdir -p src/${file%.*}/ && mv
$file src/${file%.*}/; done  
# Copy the test project files  
ONBUILD COPY test/*/*.csproj ./  
ONBUILD RUN for file in $(ls *.csproj); do mkdir -p test/${file%.*}/ && mv
$file test/${file%.*}/; done  
  
ONBUILD RUN sh ./build.sh build.cake --target=Restore  
  
ONBUILD COPY ./test ./test  
ONBUILD COPY ./src ./src  
  
# Build and Test the app  
ONBUILD RUN ./build.sh build.cake --target=Build && ./build.sh build.cake
--target=Test

