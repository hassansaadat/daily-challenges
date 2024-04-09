# Linux Setup

## Primary
```bash
sudo apt-get update
sudo apt-get install 
  vim \
  git \
  curl \
  vlc \
  net-tools
```

## Guake
```bash
sudo apt-get install guake
```
[import/export preferences](https://askubuntu.com/a/1164329)
```bash
guake --restore-preferences guake-preferences 
guake --save-preferences guake-preferences
```

## ZSH
```bash
sudo apt-get install zsh
```

### [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## [Zsh plugins](https://gist.github.com/n1snt/454b879b8f0b7995740ae04c5fb5b7df)

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
```

[fix auto-complete bug](https://gist.github.com/n1snt/454b879b8f0b7995740ae04c5fb5b7df?permalink_comment_id=4849418#gistcomment-4849418)
```bash
cd $ZSH_CUSTOM/plugins/zsh-autocomplete
git pull --tags
git reset --hard 23.05.24
```

copy .zshrc into home dir

## [Docker](https://docs.docker.com/engine/install/ubuntu/)
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

ubuntu
```bash
# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
mint
```bash
# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$UBUNTU_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

make docker work without sudo
```bash
sudo usermod -aG docker $USER
```
then restart

work
```bash
docker login
docker pull hello-world
```

## [K8S](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

### kubectl
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```

### [krew](https://krew.sigs.k8s.io/docs/user-guide/setup/install/)
```bash
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```

add this to .zshrc (already is in it)
```bash
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

restart shell and test
```bash
kubectl krew
```

### [plugins](https://krew.sigs.k8s.io/plugins/)
oidc-login
```bash
krew install oidc-login
```

context management
```bash
kubectl krew install ctx
```

context and namespace show in terminal (already exists in .zshrc)
```bash
plugins=(
  kube-ps1
)

PROMPT='$(kube_ps1)'$PROMPT # or RPROMPT='$(kube_ps1)'
```

## Python tools
```bash
sudo apt-get install python3-pip python3-dev python3-venv
```
