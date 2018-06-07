FROM didstopia/rust-server  
  
MAINTAINER didstopia  
  
# Copy Oxide into place  
RUN mkdir -p /oxide  
RUN curl -sL https://github.com/OxideMod/Snapshots/raw/master/Oxide-
Rust_Linux.zip | bsdtar -xvf- -C /oxide  
RUN chmod +x /oxide/CSharpCompiler && chmod +x /oxide/CSharpCompiler.x86  

