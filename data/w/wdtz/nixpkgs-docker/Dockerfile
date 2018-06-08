FROM busybox  
  
RUN addgroup -S nixbld && \  
for n in $(seq 1 10); do \  
adduser \  
-s /bin/false \  
-G nixbld \  
-H \  
-S \  
-D \  
nixbld$n; \  
done && \  
adduser -D --gecos '' user && \  
mkdir -m 0755 /nix && chown user /nix && \  
echo ". /home/user/.nix-profile/etc/profile.d/nix.sh" >> /etc/profile  
  
USER user  
ENV USER user  
WORKDIR /home/user  
  
RUN dir=`mktemp -d` && trap 'rm -rf "$dir"' EXIT && \  
wget -O-
http://nixos.org/releases/nix/nix-1.11.13/nix-1.11.13-x86_64-linux.tar.bz2 |
bzcat | tar x -C $dir && \  
sh $dir/*/install && \  
find /nix/store -type f -exec chmod -w {} ';' && \  
. /etc/profile && \  
nix-env -u && \  
nix-collect-garbage --delete-old && \  
nix-store --optimize && \  
nix-env -q  
  
ONBUILD ENV PATH /home/user/.nix-profile/bin:/home/user/.nix-
profile/sbin:/bin:/sbin:/usr/bin:/usr/sbin  
ONBUILD ENV ENV /etc/profile  
ENV ENV /etc/profile  

