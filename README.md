# YARC - Yet Another Recon Combine

Inspired by Jann Moon's Enumerating Esoteric Attack Surfaces 

## Prerequisites

```
apt install ansible ansible-core
```
OR
```
pipx install --include-deps ansible
```
## Installation

```
git clone ...
# fill api keys
```


## Usage
```
ansible-playbook yet-another-recon-combine/playbook.yml #-vv

Input TLD: deiteriy.com
PLAY [Recon via a given TLD] *********************
```

## TODO

- [] community.general.pipx
- [] ip & asn enum
- [] parse ANY
- [] notify in handlers
- [] nmap scan ?