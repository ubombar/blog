{
  description = "blog.bombar.dev";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "aarch64-darwin" "x86_64-darwin" "x86_64-linux" "aarch64-linux" ];
      forAll = f: nixpkgs.lib.genAttrs systems (s: f nixpkgs.legacyPackages.${s});
      python = pkgs: pkgs.python3.withPackages (ps: [ ps.markdown ]);
    in {
      # nix build -> ./result is the deployable site
      packages = forAll (pkgs: {
        default = pkgs.runCommand "blog" { nativeBuildInputs = [ (python pkgs) ]; } ''
          cp -r ${./.} src && chmod -R u+w src
          python src/build.py
          cp -r src/_site $out
        '';
      });

      devShells = forAll (pkgs: {
        default = pkgs.mkShell { packages = [ (python pkgs) pkgs.gnumake ]; };
      });
    };
}
